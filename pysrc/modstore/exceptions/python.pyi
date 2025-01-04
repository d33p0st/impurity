from typing import List

class TypeCastError(Exception):
    """`Cannot TypeCast into given type.`"""
    ...
class ListError(Exception):
    """`Generic List Error Exception`"""
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

class NodeError(Exception):
    """`Generic Node Error Exception`"""
    ...

class LinkedListError(Exception):
    """`Generic LinkedList Error Exception`"""
    PARAM_GT_ZERO: str
    PARAM_NOT_ZERO_OR_LESS: str
    PARAM_GT_EQ_ZERO: str
    PARAMS_NOT_NONE: str

class HashMapError(Exception):
    """`Generic HashMap Error Exception`"""
    ...

class TreeError(Exception):
    """`Generic Tree Error Exception`"""
    ...

class QueueError(Exception):
    """`Generic Queue Error Exception`"""
    ...

__all__: List[str]