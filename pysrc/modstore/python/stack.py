from typing import Union, Any, Iterable
from ..exceptions.python import StackOverFlow, StackUnderFlow, StackError

class Stack(list):
    def __init__(self, create_from: Union[list[Any], Iterable] = [], capacity: Union[int, None] = None) -> None:
        for value in create_from:
            super().append(value)
        
        self._capacity = capacity
    
    def __setitem__(self, index, value):
        raise StackError("Stack does not support assignment via [].")
    
    def __getitem__(self, index):
        raise StackError("Stack does not support accessing of elements via [].")
    
    def __delitem__(self, index):
        raise StackError("Stack does not support deletion via [].")
    
    @property
    def top(self) -> int:
        return super().__len__() - 1

    @property
    def pop(self) -> Any:
        """
        `Pops an element from the top.`

        Raises StackUnderFlow Exception if Stack is Empty
        """
        try:
            value = super().pop(-1)
        except IndexError:
            raise StackUnderFlow("Stack is empty.")
        
        return value
    
    def push(self, value: Any):
        if self._capacity is None:
            super().append(value)
        elif self.top == self._capacity - 1:
            raise StackOverFlow("Stack is Full.")
        else:
            super().append(value)
    
    @property
    def peek(self) -> Any:
        if self.top == -1:
            raise StackUnderFlow("Stack is empty.")
        
        return super().__getitem__(self.top)
    
    @property
    def isEmpty(self) -> bool:
        return self.top == -1
    
    @property
    def size(self) -> int:
        return self.top + 1
    
    @property
    def capacity(self) -> Union[float, int]:
        return self._capacity if self._capacity is not None else float('inf')