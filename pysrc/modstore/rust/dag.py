from .._binaries import DAG as _dag_inner, DAGChain as _chain_inner, Transaction as _transaction_inner
from typing import Literal, Union, List, Tuple

import pickle

class DAG:
    """`DAG class (Directed Acyclic Graph)`"""
    @staticmethod
    def BytesToObject(bytes: bytes) -> object:
        """`Converts any byte data to its original object form.`"""
        return pickle.loads(bytes)
    
    @staticmethod
    def ObjectToBytes(obj: object) -> bytes:
        """`Converts any object to Bytes.`"""
        return pickle.dumps(obj)

    class BasicDag:
        """`Basic DAG Class`"""
        def __init__(self):
            """`Create a basic DAG`"""
            self.dag = _dag_inner()

        def addNode(self, node: str) -> None:
            """`Add a node to the DAG`"""
            self.dag.add_node(node)
        
        def addEdge(self, from_node: str, to_node: str, force: bool = False) -> bool:
            """`Add an edge between two nodes.`
            
            - Returns True if the edge is made, if not, Returns False (False when edge makes the DAG cyclic.)
            - `Force`: if set to True, any edge that is not added, will be added and then the edge will be created.
            - Raises NotImplementedError if the any of the node is not added.
            `"""
            if not force:
                if from_node not in self.nodes or to_node not in self.nodes:
                    raise NotImplementedError("A node is not defined, cannot add Edge")
            else:
                if from_node not in self.nodes:
                    self.addNode(from_node)
                if to_node not in self.nodes:
                    self.addNode(to_node)

            try:
                self.dag.add_edge(from_node, to_node)
            except ValueError:
                return False
            
            return True
        
        @property
        def toString(self) -> str:
            """`Returns string representation of the DAG`"""
            return self.dag.to_string()
        
        @property
        def nodes(self) -> List[str]:
            """`Returns a list of added nodes.`"""
            return self.dag.list_nodes()
        
        @property
        def edges(self) -> List[Tuple[str, str]]:
            """`Returns a list of tuple[str, str] representing edges.`"""
            return self.dag.list_edges()
        
        def __str__(self) -> str:
            return self.toString
    
    class Transaction:
        """`This is a place holder, Do not try to init this class`"""
        def __init__(self, transaction: _transaction_inner) -> None:
            """`Do not init this class.`"""
            self.transaction = transaction
        
        @property
        def id(self) -> str:
            """`Returns the id of the Transaction`"""
            return self.transaction.get_id()

        @property
        def parents(self) -> List[str]:
            """`Returns a list[str] containing the parents.`"""
            return self.transaction.get_parents()
        
        def data(self, return_original: bool = False) -> Union[str, bytes, object]:
            """`Returns the Transaction Data`
            
            If `return_original` is set to True, this method will return
            the original form of the data that was added into the Transaction DAG.
            `"""
            data = self.transaction.get_data()
            if type(data) == str:
                return data
            
            if return_original:
                try:
                    return DAG.BytesToObject(data)
                except (pickle.UnpicklingError, KeyError):
                    return data

    class TransactionBased:
        """`Transaction-Based DAG Class`"""
        def __init__(self):
            """`Create a Transaction-Based DAG`"""
            self.dag = _chain_inner()
        
        def addTransaction(self, data: Union[str, bytes, object], parents: List[str]) -> str:
            """`Add a Transaction into the DAG`
            
            `data`: data can be any str, bytes or object such as list or dict.
            """
            if type(data) != str and type(data) != bytes:
                data = DAG.ObjectToBytes(data)
            
            return self.dag.add_transaction(data, parents)
        
        @property
        def valid(self) -> bool:
            """`Returns True if there are no cycles else returns False`"""
            return self.dag.is_valid()
        
        @property
        def transactions(self) -> List[str]:
            """`Returns a list of all transactions.`"""
            return self.dag.get_transactions()
        
        def transaction(self, id: str) -> 'DAG.Transaction':
            """`Returns a Transaction with id if exists else raises Value Error.`"""
            return DAG.Transaction(self.dag.get_transaction(id))

    def __init__(self, type: Literal['Basic', 'Transaction-Based']):
        """`Create a new DAG`"""

        if type == 'Basic':
            self.dag = self.BasicDag()
        else:
            self.dag = self.TransactionBased()
    
    @property
    def resolve(self):
        return type(self.dag)
    
    @property
    def create(self):
        return self.dag