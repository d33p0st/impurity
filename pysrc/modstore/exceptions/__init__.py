from .python import (
    StackError,
    StackOverFlow,
    StackUnderFlow,
    TypeCastError
)

__all__ = [
    "StackError",
    "StackOverFlow",
    "StackUnderFlow",
    "TypeCastError"
]

import importlib
module = importlib.import_module(".exceptions.python", "modstore")

def import_list_exceptions():
    for name in module.__list__:
        globals()[name] = getattr(module, name)

def import_stack_exceptions():
    for name in module.__stack__:
        globals()[name] = getattr(module, name)
