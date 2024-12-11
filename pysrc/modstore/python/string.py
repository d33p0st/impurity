
from typing import Union, Any, List as basiclist
from .list import List

class String(str):
    def __init__(self, __from__: Union[str, 'String', None, Any] = None) -> None:
        pass

    def __new__(cls, __from__: Union['String', str, None] = None) -> 'String':
        if isinstance(__from__, String):
            return super().__new__(cls, str(__from__))
        elif isinstance(__from__, str):
            return super().__new__(cls, __from__)
        elif __from__ is None:
            return super().__new__(cls, '')
        else:
            return super().__new__(cls, str(__from__))
    
    def contains_any(self, keywords: Union[basiclist[str], List[str]]) -> bool:
        for keyword in keywords:
            if keyword in self:
                return True
        
        return False