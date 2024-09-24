from .._binaries import BlockChain as _bc_inner, Block as _b_inner

from typing import Literal, Union, Pattern
import pickle

class Block:
    """`Safe Wrapper of the Block Class from binaries. Not to be called, use only methods.`
    
    `Some methods of BlockChain Class returns this class, use only the methods!`
    `"""
    def __init__(self, block: _b_inner) -> None:
        """`Not to be called! Some methods of BlockChain class returns this class. Use only the methods. Do not define this class for any purpose.`"""
        self.block = block
    
    @property
    def index(self) -> int:
        """`Index of the Block`"""
        return self.block.get_index()

    @property
    def timestamp(self) -> str:
        """`Timestamp of the Block`"""
        return self.block.get_timestamp()

    @property
    def identifier(self) -> str:
        """`Unique Identifier of the Block`"""
        return self.block.get_identifier()
    
    def data(self, return_original: bool = False) -> Union[str, bytes, object]:
        data = self.block.get_data()
        if type(data) == str:
            return data
        
        if return_original:
            try:
                return BlockChain.convertBytesToObject(data)
            except pickle.UnpicklingError:
                return data
    
    @property
    def previous_hash(self) -> str:
        """`Hash of the previous block`"""
        return self.block.get_previous_hash()

    @property
    def hash(self) -> str:
        """`Hash of the current Block`"""
        return self.block.get_hash()

class BlockChain:
    """`BlockChain Class`"""
    def __init__(self, difficulty: int = 2, timezone: Union[Literal['UTC', 'IST'], Pattern] = 'IST') -> None:
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

        ### `Usage Examples`

        ```python
        >>> from modstore.rust import BlockChain
        >>> blockchain = BlockChain(difficulty=4, timezone='UTC')
        ```
        """
        # define the blockchain
        self.blockchain = _bc_inner(difficulty, timezone)
    
    @staticmethod
    def convertObjectToBytes(obj: object) -> bytes:
        """`Convert any object to bytes`"""
        return pickle.dumps(obj)

    @staticmethod
    def convertBytesToObject(bytes: bytes) -> object:
        """`Convert any converted (object -> bytes) back to object`"""
        return pickle.loads(bytes)

    def addBlock(self, uniqueIdentifier: str, data: Union[object, str, bytes]) -> None:
        """`Add a block of data to the blockchain.`
        
        `uniqueIdentifier`: Unique Identifier for this block and its data.

        `data`: Data can be either bytes or str or any object. Except str, and excluding
        bytes any object will be converted to bytes.

        ### `Usage`

        ```
        >>> from modstore.rust import BlockChain
        >>> blockchain = BlockChain(4, 'IST')
        >>> blockchain.addBlock(uniqueIdentifier="StringData1", data="Hello, This is a Demo Data")

        # to print
        >>> print(blockchain)
        ```

        `NOTE`: If you are curious as to how to convert Any object to bytes,
        use the `BlockChain.convertObjectToBytes` method.

        ```
        # Exmaple
        >>> from modstore.rust import Blockchain

        >>> class Demo:
        ...     def __init__(self):
        ...         pass
        ... 

        # If you want to convert this class to bytes
        >>> classobj = Demo()
        >>> classbytes: bytes = BlockChain.convertObjectToBytes(classobj)
        ```
        `Similarly, other objects which are not either bytes or str will be converted to bytes
        using this method internally, Or you can do it on your own and pass the bytes in the
        addBlock method.`

        `NOTE`: Complement to the above Object to Bytes conversion, There is a method
        called `BlockChain.convertBytesToObject` which can be used to convert the converted
        (object -> bytes) back to object. `This will throw error if bytes which are not converted
        by the **BlockChain.convertObjectToBytes** method. are passed as a parameter`.
        """
        # handle objects
        if type(data) != str and type(data) != bytes:
            data = BlockChain.convertObjectToBytes(data)
        
        # call the addblock function
        self.blockchain.addblock(uniqueIdentifier, data)
    
    @property
    def valid(self) -> bool:
        """`Returns True if the blockchain is valid else False`"""
        return self.blockchain.isvalid()

    @property
    def length(self) -> int:
        """`Returns the length of the blockchain excluding the Genesis Block`"""
        return self.blockchain.length()

    def search(self, identifier: str) -> Block:
        """`Returns a block if found, else raises an Exception`"""
        return Block(self.blockchain.search(identifier))
    
    def __str__(self):
        return self.blockchain.__str__()
    
    def __repr__(self):
        return self.blockchain.__repr__()
