
from modstore.rust.blockchain import BlockChain

class obj3:
    def __init__(self):
        pass

    def add(self, a: int, b: int) -> int:
        return a + b

def test_blockchain():
    blockchain = BlockChain(2, 'IST')
    
    obj1: str = "abcd"
    obj2: bytes = "xyz".encode()
    
    blockchain.addBlock("string", obj1)
    blockchain.addBlock("bytes", obj2)
    blockchain.addBlock("class", obj3)

    assert blockchain.length == 3
    assert blockchain.valid == True

    assert blockchain.search("string").data(True) == "abcd"
    assert blockchain.search("bytes").data(True) == "xyz".encode()
    assert blockchain.search("class").data(True) == obj3