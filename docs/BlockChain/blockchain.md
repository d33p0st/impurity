## BlockChain docs

Blockchain is a decentralized digital ledger that securely records transactions across multiple computers, ensuring data transparency, security, and immutability. It's most well-known as the underlying technology behind cryptocurrencies like Bitcoin, but its use extends far beyond digital currencies to areas such as supply chain management, healthcare, finance, and more.

### Features

- **Immutability**: Once data is added to the blockchain, it is nearly impossible to alter without the consensus of the majority of nodes in the network, providing tamper resistance.

- **Consensus Mechanisms**: Blockchain operates using consensus algorithms like Proof of Work (PoW) or Proof of Stake (PoS), ensuring that all nodes agree on the validity of transactions.

- **Chain Validation**: Includes functionality to ensure the blockchain remains valid and unaltered by checking block hashes and links.

- **Hashing**: Implement cryptographic hashing (e.g., SHA-256) for generating unique block hashes.

- **Searching**: Search through the blockchain for specific blocks.

### Usage

Let us now Jump to usage now!

- [Installation](#simply-begin-by-installing-modstore)
- [Import](#import-the-blockchain-class-under-the-rust-module-of-modstore-package)
- [Create BlockChain](#create-an-initial-blockchain)
- [Add Blocks](#now-lets-add-blocks-in-our-blockchain)
- [Find Length of BlockChain](#to-find-length-of-the-blockchain)
- [Check Validity of the Blockchain](#to-check-validity-and-proof-of-work-of-the-blockchain-in-terms-of-difficulty)
- [Search and Return a Block](#to-search-for-a-block-in-the-blockchain)
- [Print the Blockchain](#to-print-the-blockchain)

##### Simply begin by installing `modstore`

```bash
pip install modstore
```

##### import the `BlockChain` Class under the rust module of `modstore` package

```python
from modstore.rust import BlockChain
```

##### Create an initial BlockChain

```python
blockchain = BlockChain() # for additional Parameters, check stubs or docstring.
```

##### Now lets Add blocks in our blockchain

```python
blockchain.addBlock("block1", data="Hello, This is a demo sentence.")
# data can be any str, any object(list, dict, class, tuple, etc) or bytes.
```

##### To find length of the blockchain

```python
length = blockchain.length
```

##### To check validity and proof of work of the blockchain (in terms of difficulty)

```python
if blockchain.valid:
    print("Blockchain is consistent and tamper proof")
else:
    print("Blockchain is tampered with.")

# remember, to tamper the blockchain a lot of computational power is needed.
# Also, since ther is no tampering function written into the rust backend,
# To tamper it, a lot of time is needed to create that.
```

##### To search for a block in the blockchain

```python
try:
    expected_block = blockchain.search(identifier="block1")
except Exception as e:
    print("Failed to find block \'block1\' on the blockchain. No such block found!")
```

##### To print the blockchain

```python
# the inbuilt methods are already set for this purpose
# and all you need to do is use the print function

print(blockchain)
```

### Source Directory Locations.

Rust Source for Blockchain: [`/src/blockchain.rs`](/src/blockchain.rs)

Raw Python Binding of the BlockChain: `/pysrc/modstore/_binaries[...].so`

Python Binding for safe execution of BlockChain: [`/pysrc/modstore/rust/blockchain.py`](/pysrc/modstore/rust/blockchain.py)

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