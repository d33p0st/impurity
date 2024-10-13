from typing import List

class TypeCastError(Exception):
    """`Cannot TypeCast into given type.`"""
    ...
class StackOverFlow(Exception):
    """`Stack is Full.`"""
    ...
class StackUnderFlow(Exception):
    """`Stack is empty`"""
    ...
class StackError(Exception):
    """`Generic Stack Error Exception`"""
    ...

__all__: List[str]
__list__: List[str]
__stack__: List[str]