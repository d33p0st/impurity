## DAG docs

A `Directed Acyclic Graph (DAG)` is a data structure where nodes are connected by directed edges, and the graph has no cycles. This structure is often used in blockchain-like applications to overcome some of the limitations of traditional blockchains, such as scalability and transaction speed. DAGs enable asynchronous, non-linear processing of transactions, where multiple transactions can be confirmed simultaneously.

### Features

- **No Mining**: In many DAG-based networks, there’s no need for miners, as transactions themselves play the role of confirming other transactions.

- **Scalability**: DAG-based systems can process multiple transactions simultaneously, leading to faster transaction times compared to traditional blockchains.

- **No Blocks**: Instead of grouping transactions into blocks, each transaction references one or more previous transactions, creating a web-like structure.

- **High Throughput**: Because of the parallel nature, DAG is highly suitable for applications requiring high throughput like IoT, micropayments, or supply chain management.

### Usage

Now let us jump to usage.

- [Installation](#installation)
- [import](#import-the-relevant-class)
- [Init](#init)
  - [Basic DAG](#basic-dag)
    - [Add Nodes](#add-nodes)
    - [Add Edges](#add-edges)
    - [List Edges and Nodes](#list-of-edges-and-nodes)
    - [Print/Get String Representation](#print-or-get-the-dag-in-string-form)
  - [Transaction Based DAG](#transaction-based-dag)
    - [Add Transaction](#add-transaction)
    - [Validity](#check-validity-of-the-dag-ledger)
    - [Get all Transactions](#get-all-transactions)
    - [Get a Transaction by Transaction ID](#get-a-transaction-by-id)
    - [Transaction Class](#transaction-class)

##### Installation

```bash
pip install modstore
```

##### import the relevant class

```python
from modstore.rust import DAG
```

##### Init

Now there are two types of DAGs available under the DAG class.

> Basic DAG

###### Basic DAG

```python
dag: DAG.BasicDag = DAG(type='Basic')
# type parameter takes only two values.
# 'Basic' and `Transaction-Based`.
```

###### Add Nodes

```python
dag.addNode('A') # add node A
dag.addNode('B') # add node B
```

###### Add Edges

```python
# `addEdge` method returns True if Edge was added successfully else Returns False

if dag.addEdge('A', 'B'): # adds an edge between A and B
    print("Edge Added")

try:
    dag.addEdge('B', 'C') # will raise NotImplementedError
    # as 'C' was not added as a node.
except NotImplementedError:
    print("Edge was not added.")

if dag.addEdge('B', 'C', force=True): # this will add any 
    # node that is not added using `addNode` and then 
    # create an edge.
    print("Added Edge B->C")

# NOTE: Any Edge that you're trying to add, if that
# creates a cyclic Graph, it will return False.
if dag.addEdge('C', 'A'): # this creates a cycle
    # as A -> B, B -> C and we are trying to
    # C -> A. which is a cycle.
    print("Cycle Added") # code wont reach here.
else:
    # code will go here
    print("C -> A creates a Cycle and hence not allowed.")
```

###### List of Edges and Nodes

```python
all_edges = dag.edges # in the form [('A', 'B'), ('B', 'C')]
all_nodes = dag.nodes # in the form ['A', 'B', 'C']
```

###### Print or get the DAG in string form.

```python
# print
print(dag) # will print the dag.

# get in string form
string_representation = dag.toString
```

> Transaction Based DAG (Simulation of DAG used in [IOTA](https://www.iota.org)).

###### Transaction Based DAG

```python
dag: DAG.TransactionBased = DAG(type='Transaction-Based')
```

###### Add Transaction

```python
# NOTE: Transaction Data can be any of there:
# str, bytes, object (list, dict, class or any other object)

# INTERNAl WORKING: 
# If str | bytes are provided, it will be taken as it is.
# if object is provided, it will be converted to bytes
# using DAG.ObjectToBytes(obj) static method.
# similarly, when getting the transaction back from DAG,
# to get the original data back,
# it uses DAG.BytesToObject(bytes) to return the original
# object or str or bytes.

demo_transaction_id = dag.addTransaction(data = "This is a DEMO", parents = [])
```

###### Check Validity of the DAG Ledger.

```python
if dag.valid:
    print("Ledger is valid.")
else:
    print("Ledger is invalid.")
```

###### Get All Transactions

```python
all_transactions = dag.transactions # returns a list of all transaction ids
```

###### Get a Transaction by ID

```python
# NOTE: the `transaction` method returns a `Transaction` type
# value, which contains some inbuilt methods that can be callable to get info about the transaction.
```

```python
# Stubs for `transaction` method
    def transaction(self, id: str) -> Transaction:
        """`Returns a Transaction with id if exists else raises Value Error.`"""
        ...
```

```python
# get a transaction by ID
transaction = dag.transaction(id=demo_transaction_id) # returns a Transaction.
```

>> #### Transaction class

```python
# the Transaction type has three methods.

# method 1: id
id_of_transaction = transaction.id # str

# method 2: parents
parents_of_transaction = transaction.parents # list[str]

# method 3: data
# NOTE: The data as said earlier could be str | bytes | object.
transaction_data = transaction.data()

# NOTE: if str or bytes was passed, this method will return the same.
# IF Object was passed as a data it is better to use
# `return_original` parameter of the `transaction.data()` method.

transaction_data = transaction.data(return_original=True)
# this returns either str or bytes or object, whatever was
# used in original form.
```

### Source Directory Locations.

Rust Source for DAG: [`/src/dag.rs`](/src/dag.rs)

Raw Python Binding of the DAG: `/pysrc/modstore/_binaries[...].so`

Python Binding for safe execution of DAG: [`/pysrc/modstore/rust/dag.py`](/pysrc/modstore/rust/dag.py)

### Install from scratch

> Make sure you have cargo installed (Rust) and VS Build Tools for C++ (for windows)

```bash
git clone https://github.com/d33p0st/modstore.git
python -m pip install --upgrade pip
pip install maturin
cd modstore
maturin develop
pip install .
```

### Issues

Feel free to submit any issues with the BlockChain Class [here](https://github.com/d33p0st/modstore/issues).

### Pull Requests

Submit pull requests [here](https://github.com/d33p0st/modstore/pulls).