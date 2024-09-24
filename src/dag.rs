use pyo3::{prelude::*, types::{PyBytes, PyString}};
use std::collections::{HashMap, HashSet};
use serde::{Serialize, Deserialize};
use sha2::{Digest, Sha256};
use serde_json;

#[derive(Debug, Clone)]
struct DAGInner {
    nodes: HashMap<String, HashSet<String>>,
}

impl DAGInner {
    fn new() -> DAGInner {
        Self {
            nodes: HashMap::new(),
        }
    }

    fn add_node(&mut self, node: String) {
        self.nodes.entry(node).or_insert(HashSet::new());
    }

    fn add_edge(&mut self, from_: String, to_: String) -> Result<(), &'static str> {
        // Check if adding this edge would create a cycle
        if self.would_create_cycle(&from_, &to_) {
            return Err("Adding this edge would create a cycle.");
        }

        // Ensure both nodes exist in the graph
        self.nodes.entry(from_.clone()).or_insert(HashSet::new());
        self.nodes.entry(to_.clone()).or_insert(HashSet::new());

        // Add the edge
        if let Some(children) = self.nodes.get_mut(&from_) {
            children.insert(to_);
        }
        Ok(())
    }

    // Checks if adding an edge would create a cycle (DFS check)
    fn would_create_cycle(&self, from: &String, to: &String) -> bool {
        let mut visited = HashSet::new();
        self.dfs(to, from, &mut visited)
    }

    // Performs a depth-first search to detect cycles
    fn dfs(&self, current: &String, target: &String, visited: &mut HashSet<String>) -> bool {
        if current == target {
            return true;
        }
        if !visited.insert(current.clone()) {
            return false;
        }
        if let Some(children) = self.nodes.get(current) {
            for child in children {
                if self.dfs(child, target, visited) {
                    return true;
                }
            }
        }
        false
    }

    // Returns the string representation of the DAG
    fn to_string(&self) -> String {
        let mut result = String::new();
        for (node, children) in &self.nodes {
            result.push_str(&format!("Node {}: {:?}\n", node, children));
        }
        result
    }

    fn list_nodes(&self) -> Vec<String> {
        self.nodes.keys().cloned().collect()
    }

    fn list_edges(&self) -> Vec<(String, String)> {
        let mut edges = Vec::new();
        for (from, children) in &self.nodes {
            for to in children {
                edges.push((from.clone(), to.clone()));
            }
        }
        edges
    }
}

#[pyclass]
pub struct DAG {
    dag: DAGInner,
}

#[pymethods]
impl DAG {
    #[new]
    fn new() -> Self {
        DAG {
            dag: DAGInner::new(),
        }
    }

    fn add_node(&mut self, node: String) {
        self.dag.add_node(node);
    }

    fn add_edge(&mut self, from_: String, to_: String) -> PyResult<()> {
        match self.dag.add_edge(from_, to_) {
            Ok(_) => Ok(()),
            Err(e) => Err(pyo3::exceptions::PyValueError::new_err(e)),
        }
    }

    fn to_string(&self) -> String {
        self.dag.to_string()
    }

    fn list_nodes(&self) -> Vec<String> {
        self.dag.list_nodes()
    }

    fn list_edges(&self) -> Vec<(String, String)> {
        self.dag.list_edges()
    }
}

// Actual Transaction based DAG

#[derive(Debug, Clone, Serialize, Deserialize)]
enum DAGDATA {
    String(String),
    Bytes(Vec<u8>),
}

impl DAGDATA {
    fn to_py_object(&self, py: Python<'_>) -> PyObject {
        match self {
            DAGDATA::String(s) => s.to_object(py),
            DAGDATA::Bytes(b) => PyBytes::new_bound(py, b).to_object(py),
        }
    }
}

#[derive(Debug, Serialize, Deserialize)]
struct TransactionInner {
    id: String,
    data: DAGDATA,
    parents: Vec<String>,
}

impl TransactionInner {
    fn new(data: PyObject, parents: Vec<String>, py: Python<'_>) -> Result<TransactionInner, std::io::Error> {
        if let Ok(pystr) = data.downcast_bound::<PyString>(py) {
            let dat = pystr.to_string_lossy().into_owned();
            let id = TransactionInner::calculate_id(&DAGDATA::String(dat.clone()), &parents);
            return Ok(TransactionInner {
                id,
                data: DAGDATA::String(dat),
                parents,
            });
        }

        if let Ok(pybytes) = data.downcast_bound::<PyBytes>(py) {
            let dat = pybytes.as_bytes().to_vec();
            let id = TransactionInner::calculate_id(&DAGDATA::Bytes(dat.clone()), &parents);
            return Ok(TransactionInner {
                id,
                data: DAGDATA::Bytes(dat),
                parents,
            });
        }

        Err(std::io::Error::new(std::io::ErrorKind::Unsupported, "Only Bytes or String is supported."))
    }

    fn calculate_id(data: &DAGDATA, parents: &Vec<String>) -> String {
        let relevant_data = (
            data,
            parents,
        );

        let data_in_string = serde_json::to_string(&relevant_data).unwrap_or_else(|_e| {
            eprintln!(
                "Failed to convert Transaction data to Serialized String: {}",
                _e
            );
            std::process::exit(1);
        });

        let mut hasher = Sha256::new();
        hasher.update(data_in_string);
        format!("{:x}", hasher.finalize())
    }
}

#[pyclass]
pub struct DAGChain {
    transactions: HashMap<String, TransactionInner>,
}

#[pymethods]
impl DAGChain {
    #[new]
    pub fn new() -> PyResult<DAGChain> {
        Ok(Self {
            transactions: HashMap::new(),
        })
    }

    pub fn add_transaction(&mut self, data: PyObject, parents: Vec<String>, py: Python<'_>) -> PyResult<String> {
        let transaction = match TransactionInner::new(data, parents, py) {
            Ok(t) => t,
            Err(e) => {
                eprintln!("Failed to Add Transaction: {}", e);
                std::process::exit(1);
            }
        };

        let id = transaction.id.clone();
        self.transactions.insert(id.clone(), transaction);
        Ok(id)
    }

    pub fn is_valid(&self) -> PyResult<bool> {
        let mut confirmed = HashSet::new();
        for transaction in self.transactions.values() {
            if transaction.parents.is_empty() {
                confirmed.insert(transaction.id.clone());
            } else {
                for parent in &transaction.parents {
                    if !self.transactions.contains_key(parent) {
                        return Ok(false);
                    }
                    confirmed.insert(transaction.id.clone());
                }
            }
        }
        Ok(true)
    }

    pub fn get_transactions(&self) -> PyResult<Vec<String>> {
        Ok(self.transactions.keys().cloned().collect::<Vec<String>>())
    }

    pub fn get_transaction(&self, id: &str) -> PyResult<Transaction> {
        match self.transactions.get(id) {
            Some(transaction) => {
                let data: PyObject = Python::with_gil(|py| {
                    transaction.data.to_py_object(py)
                });

                return Ok(
                    Transaction {
                        id: transaction.id.clone(),
                        data,
                        parents: transaction.parents.clone(),
                    }
                );
            },
            None => Err(pyo3::exceptions::PyValueError::new_err(format!("No transaction with id {} found on the DAG", id))),  // Return an empty list if not found
        }
    }
}

#[pyclass]
pub struct Transaction {
    id: String,
    data: PyObject,
    parents: Vec<String>,
}

#[pymethods]
impl Transaction {
    pub fn get_data(&self, py: Python<'_>) -> PyResult<PyObject> {
        Ok(self.data.clone_ref(py))
    }

    pub fn get_id(&self) -> PyResult<String> {
        Ok(self.id.clone())
    }

    pub fn get_parents(&self) -> PyResult<Vec<String>> {
        Ok(self.parents.clone())
    }
}