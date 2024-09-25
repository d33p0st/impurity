"""This file represents the raw rust module implementation.
Precautions are needed for usage.
If not a developer, do not use this.
"""

from typing import Literal, Union, Pattern, List, Tuple

class Block:
    """# `Not to be called.`"""
    def __init__(self, index: int, timestamp: str, data_identifier: str, data: object, previous_hash: str, hash: str) -> None:
        """# `Not to be called.`"""
        ...
    
    def get_index(self) -> int:
        """`Returns index of the Block`"""
        ...
    
    def get_timestamp(self) -> str:
        """`Returns the timestamp of the Block`"""
        ...
    
    def get_identifier(self) -> str:
        """`Returns the identifier of the Block`"""
        ...
    
    def get_data(self) -> object:
        """`Returns the data in the block`"""
        ...
    
    def get_previous_hash(self) -> str:
        """`Returns the hash of the previous block`"""
        ...
    
    def get_hash(self) -> str:
        """`Returns the hash of the block`"""
        ...

class BlockChain:
    """`BlockChain Class`"""
    def __init__(self, difficulty: int, time: Union[Literal['UTC', 'IST'], Pattern]) -> None:
        """`Initialise a blockchain with specified difficulty and timezone to use in timestamps.`

        `Difficulty`: The difficulty specifies how many leading zeros are required for a block's 
        hash to be considered valid. A higher difficulty makes it more computationally expensive 
        to find a valid hash, thereby regulating the time between block generations and maintaining 
        the security of the blockchain. During the mining process (`mine` method (Internally)), the block repeatedly 
        computes its hash until the first `difficulty` characters of the hash match the required pattern 
        (i.e., a string of `0`s). This process involves trial and error, and the number of iterations needed 
        depends on the difficulty level.

        `time`: This parameter sets the timezone of the timestamp to be used in each block.
        This parameter takes literals ['UTC', 'IST'] or `"HH:MM:SS"` to be added to UTC to
        get the desired timezone.
        """
        ...
    
    def addblock(self, data_identifier: str, data: Union[str, bytes]) -> None:
        """`Add a block of data to the blockchain.`
        
        `data_identifier`: Unique Identifier for this block and its data.

        `data`: Data can be either bytes or str. If you need to add other data types, use the `bytes()` method
        to convert it to bytes.
        """
        ...
    
    def isvalid(self) -> bool:
        """`Check if the blockchain has been tampered or consistent.`
        
        Returns True if the blockchain is consistent else False.
        """
        ...
    
    def length(self) -> int:
        """`Returns the length of the Blockchain excluding the genesis block.`"""
        ...
    
    def search(self, identifier: str) -> Block:
        """`Returns a block if found else raises an exception.`"""
        ...

class DAG:
    """`DAG class (Directed Acyclic Graph)`"""
    def __init__(self) -> None:
        """`Create a new Dag`"""
        ...
    
    def add_node(self, node: str) -> None:
        """`Add a new node to the DAG
        
        `node`: node name to add to the dag. (str)
        `"""
        ...
    
    def add_edge(self, from_: str, to_: str) -> None:
        """`Add an edge between two nodes.
        
        - Make sure to avoid cyclic edges else it will raise ValueError.
        `"""
        ...
    
    def to_string(self) -> str:
        """`Returns String Representation of the DAG`"""
        ...
    
    def list_nodes(self) -> List[str]:
        """`Returns a list of all nodes that are added.`"""
        ...
    
    def list_edges(self) -> List[Tuple[str, str]]:
        """`Returns a list of tuple(str, str) representing edges.`"""
        ...

class Transaction:
    """`Do not instantiate this class. It is a Place Holder`"""
    def get_data(self) -> object:
        """`Returns the Transaction Data`"""
        ...
    
    def get_id(self) -> str:
        """`Returns the Transaction id.`"""
        ...
    
    def get_parents(self) -> List[str]:
        """`Returns a list[str] containing the parents.`"""
        ...

class DAGChain:
    """`DAG Chain Class`"""
    def __init__(self) -> None:
        """`Create a Dag Chain`"""
        ...
    
    def add_transaction(self, data: Union[str, bytes], parents: List[str]) -> str:
        """`Add a transaction to the Dag Chain.`
        
        Returns the id of the transaction.
        """
        ...
    
    def is_valid(self) -> bool:
        """`Checks if the DAG is valid (No cycles)`
        
        Returns True if valid, else False
        """
        ...
    
    def get_transactions(self) -> List[str]:
        """`Returns a list of keys (ids) of all available transactions`"""
        ...
    
    def get_transaction(self, id: str) -> Transaction:
        """`Returns the Transaction if found, else raises ValueError`"""
        ...