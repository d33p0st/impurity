use chrono::{DateTime, Utc, Duration};
use sha2::{Sha256, Digest};
use serde::{Serialize, Deserialize};
use regex::Regex;
use pyo3::prelude::*;
use pyo3::types::{PyString, PyBytes};
use std::fmt;

#[derive(Debug, Clone, Serialize, Deserialize)]
enum BlockData {
    String(String),
    Bytes(Vec<u8>),
}

impl BlockData {
    fn to_py_object(&self, py: Python<'_>) -> PyObject {
        match self {
            BlockData::String(s) => s.to_object(py),
            BlockData::Bytes(b) => PyBytes::new_bound(py, b).to_object(py),
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
enum TimeType {
    IST,
    UTC,
    Custom(i64, i64, i64)
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct BlockInner {
    index: usize,
    timestamp: String,
    data_identifier: String,
    data: BlockData,
    previous_hash: String,
    hash: String,
    nonce: u64,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
struct BlockChainInner {
    chain: Vec<BlockInner>,
    difficulty: usize,
    time_type: TimeType,
}

impl BlockInner {
    fn new(index: usize, data_identifier: String, data: BlockData, previous_hash: String, time_type: TimeType) -> BlockInner {
        let time: DateTime<Utc>;
        match time_type {
            TimeType::IST => {
                time = Utc::now() + Duration::hours(5) + chrono::Duration::minutes(30);
            },
            TimeType::UTC => {
                time = Utc::now();
            },
            TimeType::Custom(hours, minutes, seconds) => {
                time = Utc::now() + Duration::hours(hours) + Duration::minutes(minutes) + Duration::seconds(seconds);
            }
        }

        let timestamp = time.to_rfc3339();
        let nonce = 0;

        let mut block = BlockInner {
            index,
            timestamp,
            data_identifier,
            data,
            previous_hash: previous_hash.clone(),
            hash: String::new(),
            nonce,
        };

        block.hash = block.calculate_hash();

        block
    }

    fn calculate_hash(&self) -> String {
        let relevant_data = (
            self.index,
            &self.timestamp,
            &self.data_identifier,
            &self.data,
            &self.previous_hash,
            self.nonce,
        );
        let block_data = serde_json::to_string(&relevant_data).unwrap_or_else(|_e| {
            eprintln!("Failed to generate hash for block: {}", self.index);
            std::process::exit(1);
        });

        let mut hasher = Sha256::new();
        hasher.update(block_data);
        format!("{:x}", hasher.finalize())
    }

    fn mine(&mut self, difficulty: usize) {
        let target = "0".repeat(difficulty);
        while &self.hash[..difficulty] != target {
            self.nonce += 1;
            self.hash = self.calculate_hash();
        }
    }
}

impl BlockChainInner {
    fn new(difficulty: usize, time_type: TimeType) -> BlockChainInner {
        let mut blockchain = BlockChainInner {
            chain: Vec::new(),
            difficulty,
            time_type,
        };
        blockchain.create_genesis();
        blockchain
    }

    fn create_genesis(&mut self) {
        let genesis = BlockInner::new(0, "Genesis".to_string(), BlockData::String("".to_string()), "".to_string(), self.time_type.clone());
        self.chain.push(genesis);
    }

    fn get_latest(&self) -> &BlockInner {
        self.chain.last().unwrap()
    }

    fn len(&self) -> usize {
        self.chain.len() - 1
    }

    fn add_block(&mut self, data_identifier: String, data: BlockData) {
        let prevhash = self.get_latest().hash.clone();
        let mut block = BlockInner::new(self.chain.len(), data_identifier, data, prevhash, self.time_type.clone());
        block.mine(self.difficulty);
        // println!("{} {}" ,block.hash.clone(), block.calculate_hash());
        self.chain.push(block);
    }

    fn chain_valid(&self) -> bool {
        for i in 1..self.chain.len() {
            let current_b = &self.chain[i];
            let prev_b = &self.chain[i-1];

            if current_b.hash != current_b.calculate_hash() {
                return false;
            }

            if current_b.previous_hash != prev_b.hash {
                return false;
            }

            if current_b.hash[..self.difficulty] != "0".repeat(self.difficulty) {
                return false;
            }
        }

        true
    }
}

#[pyclass]
#[derive(Debug)]
pub struct Block {
    index: usize,
    timestamp: String,
    data_identifier: String,
    data: PyObject,
    previous_hash: String,
    hash: String,
}

#[pymethods]
impl Block {
    #[new]
    fn new(index: usize, timestamp: String, data_identifier: String, data: PyObject, previous_hash: String, hash: String) -> PyResult<Block> {
        Ok(Self {
            index,
            timestamp,
            data_identifier,
            data, 
            previous_hash,
            hash,
        })
    }

    fn get_index(&self) -> PyResult<usize> {
        Ok(self.index)
    }

    fn get_timestamp(&self) -> PyResult<String> {
        Ok(self.timestamp.clone())
    }

    fn get_identifier(&self) -> PyResult<String> {
        Ok(self.data_identifier.clone())
    }

    fn get_data(&self, py: Python<'_>) -> PyResult<PyObject> {
        Ok(self.data.clone_ref(py))
    }
    
    fn get_previous_hash(&self) -> PyResult<String> {
        Ok(self.previous_hash.clone())
    }

    fn get_hash(&self) -> PyResult<String> {
        Ok(self.hash.clone())
    }
}

#[pyclass]
#[derive(Debug, Clone)]
pub struct BlockChain {
    blockchain: BlockChainInner,
}

#[pymethods]
impl BlockChain {
    #[new]
    pub fn new(difficulty: usize, time: &str) -> PyResult<BlockChain> {
        let time_regex = Regex::new(r"^\d{2}:\d{2}:\d{2}$").unwrap();

        if time.to_lowercase() == "utc" {
            Ok(Self {
                blockchain: BlockChainInner::new(difficulty, TimeType::UTC)
            })
        } else if time.to_lowercase() == "ist" {
            Ok(Self {
                blockchain: BlockChainInner::new(difficulty, TimeType::IST)
            })
        } else if !time_regex.is_match(time)  {
            let parts: Vec<&str> = time.split(":").collect();
            Ok(Self {
                blockchain: BlockChainInner::new(difficulty, TimeType::Custom(parts[0].parse().unwrap(), parts[1].parse().unwrap(), parts[2].parse().unwrap()))
            })
        } else {
            Err(pyo3::exceptions::PyValueError::new_err(format!("Time Syntax Error (invalid): {}", time)))
        }
    }

    pub fn addblock(&mut self, data_identifier: &str, data: PyObject, py: Python<'_>) -> PyResult<()> {
        if let Ok(pystr) = data.downcast_bound::<PyString>(py) {
            let dat = pystr.to_string_lossy().into_owned();
            self.blockchain.add_block(data_identifier.to_string(), BlockData::String(dat));
            return  Ok(());
        }

        if let Ok(pybytes) = data.downcast_bound::<PyBytes>(py) {
            let dat = pybytes.as_bytes().to_vec();
            self.blockchain.add_block(data_identifier.to_string(), BlockData::Bytes(dat));
            return Ok(());
        }
        
        Err(pyo3::exceptions::PyTypeError::new_err("Invalid Data type (expected string or bytes)"))
    }

    pub fn isvalid(&self) -> bool {
        self.blockchain.chain_valid()
    }

    pub fn length(&self) -> PyResult<usize> {
        Ok(self.blockchain.len())
    }

    fn __str__(&self) -> String {
        format!("{}", self.blockchain)
    }

    fn __repr__(&self) -> String {
        self.__str__()
    }

    fn search(&self, identifier: &str) -> PyResult<Block> {
        let block: Block;

        for chain in &self.blockchain.chain {
            if chain.data_identifier == identifier {
                let data: PyObject = Python::with_gil(|py| {
                    chain.data.to_py_object(py)
                });
                block = Block::new(chain.index, chain.timestamp.clone(), chain.data_identifier.clone(), data, chain.previous_hash.clone(), chain.hash.clone())?;
                return Ok(block);
            }
        }

        Err(pyo3::exceptions::PyException::new_err(format!("Failed to find {} on the blockchain!", identifier)))
    }
}

impl fmt::Display for BlockInner {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match &self.data {
            BlockData::String(_s) => {
                write!(f, "-------------------------\nBlock #{}\n-------------------------\nDataType: String\nData: {}\nTimestamp: {}\nHash: {}\n-------------------------\n", self.index, _s, self.timestamp, self.hash)
            },
            BlockData::Bytes(_b) => {
                write!(f, "-------------------------\nBlock #{}\n-------------------------\nDataType: Bytes\nData: {:?}\nTimestamp: {}\nHash: {}\n-------------------------\n", self.index, _b, self.timestamp, self.hash)
            },
        }
    }
}

impl fmt::Display for BlockChainInner {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "|--------------------------------|\n")?;
        for idx in 1..self.chain.len() {
            write!(f, "{}\n", self.chain[idx])?;
        }
        write!(f, "|--------------------------------|\n")
    }
}