use pyo3::prelude::*;
use std::collections::{HashMap, HashSet};

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