from .._binaries import DAG as _dag_inner

class DAG:
    """`DAG class (Directed Acyclic Graph)`"""
    def __init__(self):
        """`Create a new DAG`"""
        self.dag = _dag_inner()
    
    def addNode(self, node: str) -> None:
        """`Add a node to the DAG`"""
        self.dag.add_node(node)
    
    def addEdge(self, from_node: str, to_node: str) -> bool:
        """`Add an edge between two nodes.
        
        - Returns True if the edge is made, if not, Returns False (False when edge makes the DAG cyclic.)
        `"""
        try:
            self.dag.add_edge(from_node, to_node)
            return True
        except ValueError:
            return False
    
    @property
    def toString(self) -> str:
        """`Returns string representation of the DAG`"""
        return self.dag.to_string()
    
    @property
    def nodes(self) -> list[str]:
        """`Returns a list of added nodes.`"""
        return self.dag.list_nodes()
    
    @property
    def edges(self) -> list[tuple[str, str]]:
        """`Returns a list of tuple[str, str] representing edges.`"""
        return self.dag.list_edges()