`Badges`

[![Unit Tests](https://github.com/d33p0st/modstore/actions/workflows/tests.yml/badge.svg)](https://github.com/d33p0st/modstore/actions/workflows/tests.yml)
[![Build](https://github.com/d33p0st/modstore/actions/workflows/generate_wheels.yml/badge.svg)](https://github.com/d33p0st/modstore/actions/workflows/generate_wheels.yml)
[![codecov](https://codecov.io/gh/d33p0st/modstore/branch/main/graph/badge.svg?token=P27ASL6TGH)](https://codecov.io/gh/d33p0st/modstore)
[![Downloads](https://static.pepy.tech/badge/modstore)](https://pepy.tech/project/modstore)

# Modstore

This is a one stop library for all your data structure and algorithm needs. `Modstore`provides several python and rust (leveraging it's speed and reliability) based data-structures and algorithms. The Data Structures
offered by `modstore` are custom built and well-written to simulate the
structure rules.

#### Due to increasing code base, A proper README is in the works. For Convenience, all instructions are added in the docstrings of the classes and functions.

## Module Pathways for importing.

1. Data Structures

    ```python
    from modstore.datastructures import (
        # HashTable
        HashMap, # Normal Key-Value Pair Type HashTable.
        AutoHashMap, # Uses hash function for keys, user provides values.
        
        # Built-in upgrade
        List, # Modified List.
        
        # New, Stack
        Stack, # Actual Stack.

        # New, Queue
        Queue, # Queue (supports dequeue, circular implementation for definite capacity)
        PriorityQueue, # (supports dequeue, circular implementation for definite capacity)
        priority, # A class for extended PriorityQueue customization.

        # New, Singly Linked List
        SingleLinkNode, # Node class for Singly Linked List
        LinkedListOne, # Singly Linked List 

        # New, LRU Cache (implemented using singly linked list)
        LRUCache,

        # New, Doubly Linked List
        DoubleLinkNode, # Node class for doubly linked list
        LinkedListTwo, # Doubly Linked List

        # New, Blockchain
        BlockChain, # Blockchain data structure
        Block, # Block class, cannot be initialized, only for internal purposes.

        # New, Directed Acyclic Graphs (DAG)
        DAG,

        # Coming soon
        MultiLinkNode, # node class for multi nodes
        LinkedListMulti, # Multi linked list
        BinaryNode, # Node class for Binary Tree
        BinaryTree, # BinaryTree class.
    )
    ```
2. Algorithms

    ```python
    from modstore.algorithms.searching import (
        Search, # A class that contains static methods for searching
        SearchObject, # A class to define one object that can be searched using different algorithms,
    )

    from modstore.algorithms.sorting import (
        Sort, # A class that contains static methods for sorting
        SortObject, # A class to define one object that can be sorted using different algorithms.
    )
    ```
3. Prototype for [modkit](https://pypi.org/project/modkit/).

    `modkit` is a new lib for programming tools, got more than `51k` downloads in the first week. The prototype for the same can be found under:

    ```python
    from modstore.tools import (
        classtools, # aliased as override in modkit

        CustomBoolean, # aliased as Possibility in modkit

        Property, # aliased as the same name in modkit.
    )
    ```

## Install from scratch

> Make sure you have cargo installed (Rust) and VS Build Tools for C++ (for windows)

```bash
git clone https://github.com/d33p0st/modstore.git
python -m pip install --upgrade pip
pip install maturin
cd modstore
maturin develop
pip install .
```

## Issues

Feel free to submit any issues [here](https://github.com/d33p0st/modstore/issues).

## Pull Requests

Submit pull requests [here](https://github.com/d33p0st/modstore/pulls).