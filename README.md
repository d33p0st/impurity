
[![Unit Tests](https://github.com/d33p0st/modstore/actions/workflows/tests.yml/badge.svg)](https://github.com/d33p0st/modstore/actions/workflows/tests.yml)
[![Build](https://github.com/d33p0st/modstore/actions/workflows/generate_wheels.yml/badge.svg)](https://github.com/d33p0st/modstore/actions/workflows/generate_wheels.yml)
[![codecov](https://codecov.io/gh/d33p0st/modstore/branch/main/graph/badge.svg?token=P27ASL6TGH)](https://codecov.io/gh/d33p0st/modstore)
[![Downloads](https://static.pepy.tech/badge/modstore)](https://pepy.tech/project/modstore)

# Overview

`modstore` brings the speed python lacked while implementing complex data structures. Leveraging `Rust's` speed, `modstore` brings custom data structures to decrease processing time. Apart from that, `modstore` offers upgraded built-in data structures such as `list`, `dict`, `tuple` and a few new ones like `stack`.

`modstore` started as a data structure library but now also contains algorithms such as sorting and searching.

## Features

`modstore` currently offers the following data structures and algorithms to make your day an easy one:

> **For documentation on a particular topic, click on the topic.**

> **The docs for few topics are still under works, The code itself has docstring(s) in them for ease of use.**

> Here are the basic importing structures for all currently available modules.
> ```python
> from modstore.python import List, Stack
> from modstore.rust import BlockChain, DAG
> from modstore.algorithms.searching import Search, SearchObject
> from modstore.algorithms.sorting import Sort, SortObject
> ```

**Categories**

- [Algorithms](https://d33p0st.in/documentation/libraries/modstore/algorithms/#libraries "Algorithms provided under modstore")

  `modstore` contains a hell lot of detailed algorithms.

  Currently available:

  - [Searching](https://d33p0st.in/documentation/libraries/modstore/algorithms/searching/#libraries "Searching Algorithms")
    
    - Linear Search
    - Sentinel Linear Search
    - Binary Search
    - Meta Binary Search (One Sided Binary Search)
    - Ubiquitous Binary Search
    - Ternary Search
    - Jump Search
    - Interpolation Search
    - Exponential Search
    - Fibonacci search

  - [Sorting](https://d33p0st.in/documentation/libraries/modstore/algorithms/sorting/#libraries "Sorting Algorithms")

    - Selection Sort
    - Bubble Sort
    - Insertion Sort
    - Merge Sort
    - Quick Sort
    - Heap Sort
    - Counting Sort
    - Radix Sort
    - Bucket Sort
    - Tim Sort
    - Bingo Sort
    - Shell Sort
    - Comb Sort
    - Pigeonhole Sort
    - Cycle Sort
    - Cocktail Sort
    - Strand Sort
    - Sleep Sort
    - Pancake Sort
    - Bogo Sort
    - Gnome Sort
    - Stooge Sort
    - Tag Sort
    - Brick Sort
    - Three Way Merge Sort

- [Rust powered data structures](https://d33p0st.in/documentation/libraries/modstore/rust/#libraries "modstore's rust powered data structures")

  `modstore` offers the following `rust` powered data structures:

  - [BlockChain](https://d33p0st.in/documentation/libraries/modstore/rust#blockchain-docs "BlockChain Documentation"): Using Rust's performance, create tamper proof blockchain data structure of your required difficulty. Search through the blockchain and retrieve data in their original form as provided.

  - [DAG](./rust#dag-docs "DAG Documentation"): Directed Acyclic Graphs are graphs with no cycles, used in certain blockchain variants like [IOTA](https://www.iota.org "IOTA Homepage"). Create, manipulate and store Network like data in DAG ledgers.

- [Upgraded Python built-ins](https://d33p0st.in/documentation/libraries/modstore/builtins/#libraries)

  `modstore` has these upgraded built-ins:

  - [List]

- [New Python data structures](https://d33p0st.in/documentation/libraries/modstore/new/#libraries)

  - [Stack]
  <!-- - [HashMap] -->

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

Feel free to submit any issues with the BlockChain Class [here](https://github.com/d33p0st/modstore/issues).

## Pull Requests

Submit pull requests [here](https://github.com/d33p0st/modstore/pulls).