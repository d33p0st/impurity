# python exceptions

# LIST
# typecast error
class TypeCastError(Exception):
    pass

# STACK
# overflow
class StackOverFlow(Exception):
    pass
# underflow
class StackUnderFlow(Exception):
    pass
# Stack Func Err
class StackError(Exception):
    pass


# all
__all__ = [
    "TypeCastError",
    "StackError",
    "StackOverFlow",
    "StackUnderFlow"
]

__list__ = [
    "TypeCastError"
]

__stack__ = [
    "StackError",
    "StackOverFlow",
    "StackUnderFlow"
]