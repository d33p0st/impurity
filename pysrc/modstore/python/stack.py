
from typing import Iterable, Union, Type, List as basicList, Iterator, Set
from typing import Generic, TypeVar, SupportsIndex
from typing import overload

from ..exceptions.python import StackError, StackOverFlow, StackUnderFlow
from .Math.constants import Infinity

import math
import re

X = TypeVar('X')
Some = TypeVar('Some')

class Stack(Generic[X]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, *, create_from: Iterable[X] = [], capacity: Union[int, None] = None) -> None: ...

    def __init__(self, *, create_from: Iterable[X] = [], capacity: Union[int, None] = None) -> None:
        self._internal: basicList[X] = []

        for elem in create_from:
            self._internal.append(elem)
        
        self._capacity = capacity
    
        self._allow_access = False
        self._get_item_types()

    def _get_item_types(self) -> None:
        self._item_types: Set[Type] = {type(item) for item in self._internal}
    
    @overload
    def __setitem__(self, key: SupportsIndex, value: X, /) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Iterable[X], /) -> None: ...

    def __setitem__(self, key: Union[SupportsIndex, slice], value: Union[X, Iterable[X]], /) -> None:
        if not self._allow_access:
            raise StackError("Stack does not support assignment via [].")
        else:
            self._internal.__setitem__(key, value)
    
    @overload
    def __getitem__(self, how: SupportsIndex, /) -> X: ...
    @overload
    def __getitem__(self, how: slice, /) -> 'Stack[X]': ...

    def __getitem__(self, how: Union[SupportsIndex, slice], /) -> Union[X, 'Stack[X]']:
        if not self._allow_access:
            raise StackError("Stack does not support accessing of elements via [].")
        else:
            if isinstance(how, SupportsIndex):
                return self._internal.__getitem__(how)
            elif isinstance(how, slice):
                return Stack(create_from=self._internal.__getitem__(how))
    
    def __delitem__(self, key: Union[SupportsIndex, slice], /) -> None:
        if not self._allow_access:
            raise StackError("Stack does not support deletion via [].")
        else:
            self._internal.__delitem__(key)
    
    def __contains__(self, key: object, /) -> bool:
        return self._internal.__contains__(key)
    
    def __iter__(self) -> Iterator[X]:
        return self._internal.__iter__()
    
    def __reversed__(self) -> Iterator[X]:
        return self._internal.__reversed__()
    
    def __str__(self) -> str:
        return self._internal.__str__()
    
    def __repr__(self) -> str:
        return self._internal.__repr__()
    
    def __len__(self) -> int:
        return self._internal.__len__()
    
    @overload
    def __add__(self, object: Union['Stack[X]', basicList[X]], /) -> 'Stack[X]': ...
    @overload
    def __add__(self, object: Union['Stack[Some]', basicList[Some]], /) -> 'Stack[Union[X, Some]]': ...

    def __add__(self, object, /):
        if isinstance(object, Stack):
            return Stack(create_from=self._internal.__add__(object._internal))
        elif isinstance(object, basicList):
            return Stack(create_from=self._internal.__add__(object))
        else:
            raise StackError(f"Cannot add <class 'Stack'> to {type(object)}")
    
    def __mul__(self, object: SupportsIndex, /):
        return Stack(create_from=self._internal.__mul__(object))
        
    def __eq__(self, object: object, /) -> bool:
        if isinstance(object, Stack):
            return self._internal.__eq__(object._internal)
        else:
            raise StackError(f"Cannot compare Stack with {type(object)}")
    
    def __ne__(self, object: object, /) -> bool:
        return not self.__eq__(object)
    
    def __bool__(self) -> bool:
        return self.isNotEmpty
    
    def __ge__(self, object: Union['Stack[X]', Iterable[X]], /) -> bool:
        if isinstance(object, Stack):
            return self._internal.__ge__(object._internal)
        elif isinstance(object, Iterable):
            return self._internal.__ge__(list(object))
        else:
            return self._internal.__ge__(object)
    
    def __gt__(self, object: Union['Stack[X]', Iterable[X]], /) -> bool:
        if isinstance(object, Stack):
            return self._internal.__gt__(object._internal)
        elif isinstance(object, Iterable):
            return self._internal.__gt__(list(object))
        else:
            return self._internal.__gt__(object)
    
    def __iadd__(self, object: Iterable[X], /) -> 'Stack[X]':
        return Stack(create_from=self._internal.__iadd__(object))
    
    def __imul__(self, object: SupportsIndex, /) -> 'Stack[X]':
        return Stack(create_from=self._internal.__imul__(object))
    
    def __le__(self, object: Union['Stack[X]', basicList[X]], /) -> bool:
        if isinstance(object, Stack):
            return self._internal.__le__(object._internal)
        elif isinstance(object, basicList):
            return self._internal.__le__(object)
        else:
            return self._internal.__le__(object)
        
    def __lt__(self, object: Union['Stack[X]', basicList[X]], /) -> bool:
        if isinstance(object, Stack):
            return self._internal.__lt__(object._internal)
        elif isinstance(object, basicList):
            return self._internal.__lt__(object)
        else:
            return self._internal.__lt__(object)
    
    def __rmul__(self, object: SupportsIndex, /) -> 'Stack[X]':
        return Stack(create_from=self._internal.__rmul__(object))

    def __sizeof__(self) -> int:
        return self._internal.__sizeof__()
    
    def _prop_delete_error(self, prop: str) -> None:
        raise StackError(f"{prop} property cannot be deleted.")
    
    def _prop_assignment_error(self, prop: str) -> None:
        raise StackError(f"{prop} property assignment is not allowed.")
    
    @property
    def top(self) -> int:
        return self._internal.__len__() - 1
    
    @top.setter
    def top(self, value) -> None:
        return self._prop_assignment_error('Top')
    
    @top.deleter
    def top(self) -> None:
        return self._prop_delete_error('Top')
    
    def append(self, object: X) -> None:
        self._internal.append(object)
    
    def push(self, object: X) -> None:
        if self._capacity is None:
            self._internal.append(object)
        elif self.top == self._capacity - 1:
            raise StackOverFlow("Stack is currently at maximum capacity.")
        else:
            self._internal.append(object)
    
    def pop(self, garbage: bool = False) -> Union[X, None]:
        try:
            if not garbage:
                return self._internal.pop()
            else:
                g = self._internal.pop()
                del g
                return None
        except IndexError:
            raise StackUnderFlow("Stack is currently empty.")
    
    @property
    def peek(self) -> X:
        self._allow_access = True
        value = self[-1]
        self._allow_access = False
        return value
    
    @peek.setter
    def peek(self, value):
        return self._prop_assignment_error('Peek')
    
    @peek.deleter
    def peek(self):
        raise self._prop_delete_error('Peek')
    
    @property
    def isEmpty(self) -> bool:
        return self.top == -1
    
    @isEmpty.setter
    def isEmpty(self, value):
        return self._prop_assignment_error('isEmpty')
    
    @isEmpty.deleter
    def isEmpty(self):
        return self._prop_delete_error('isEmpty')
    
    @property
    def isNotEmpty(self) -> bool:
        return not self.isEmpty
    
    @isNotEmpty.setter
    def isNotEmpty(self, value):
        return self._prop_assignment_error('isNotEmpty')
    
    @isNotEmpty.deleter
    def isNotEmpty(self) -> None:
        return self._prop_delete_error('isNotEmpty')
    
    @property
    def size(self) -> int:
        return self.top + 1
    
    @size.setter
    def size(self, value) -> None:
        return self._prop_assignment_error('Size')
    
    @size.deleter
    def size(self) -> None:
        return self._prop_delete_error('Size')
    
    @property
    def capacity(self) -> Union[int, Infinity]:
        return self._capacity if self._capacity is not None else Infinity()
    
    @capacity.setter
    def capacity(self, capacity: Union[int, None]):
        self._capacity = capacity
    
    @capacity.deleter
    def capacity(self) -> None:
        self._capacity = None
    
    @property
    def sum(self) -> X:
        self._get_item_types()

        if (len(self._item_types) != 1) or (list(self._item_types)[0] not in (int, str, float)):
            raise StackError("Stack contains non-int and non-float and non-str elements OR Mixed elements of different types.")
        elif len(self._item_types) == 1:
            if list(self._item_types)[0] in (int, float):
                return sum(self._internal)
            else:
                return ''.join(self._internal)
        elif len(self._item_types) == 2 and int in self._item_types and float in self._item_types:
            return sum(self._internal)
        else:
            raise StackError("Stack contains non-int and non-float and non-str elements OR Mixed elements of different types.")
    
    @sum.setter
    def sum(self, value) -> None:
        return self._prop_assignment_error('Sum')
    
    @sum.deleter
    def sum(self) -> None:
        return self._prop_delete_error('Sum')
    
    @property
    def toList(self) -> basicList[X]:
        return self._internal
    
    @toList.setter
    def toList(self, value) -> None:
        return self._prop_assignment_error('toList')
    
    @toList.deleter
    def toList(self) -> None:
        return self._prop_delete_error('toList')
    
    def joinWith(self, sep: str = '') -> str:
        stringlist: basicList[str] = []
        for x in self._internal:
            stringlist.append(str(x))
        
        return sep.join(stringlist)
    
    @staticmethod
    def infixToPostfix(expression: str) -> str:
        stack: Stack[str] = Stack()
        result: Stack[str] = Stack()

        for character in expression:
            if is_operand(character):
                result.push(character)
            elif character == '(':
                stack.push(character)
            elif character == ')':

                while stack.isNotEmpty and stack.peek != '(':
                    result.push(stack.pop())
                stack.pop(garbage=True) # pop (
            
            elif character == " ":
                continue

            else:

                while (stack.isNotEmpty and operator_precedence(stack.peek) > operator_precedence(character)) or (stack.isNotEmpty and operator_precedence(stack.peek) == operator_precedence(character) and is_left_associative(stack.peek)):
                    result.push(stack.pop())
                stack.push(character)
        
        while stack.isNotEmpty:
            result.push(stack.pop())
        
        return result.joinWith()
    
    @staticmethod
    def infixToPrefix(expression: str) -> str:
        # Reverse the infix
        expression = expression[::-1].replace('(', '#').replace(')', '(').replace('#', ')')
        # return postfix of this in reverse.
        return Stack.infixToPostfix(expression)[::-1]

    @staticmethod
    def postfixToInfix(expression: str) -> str:
        stack: Stack[str] = Stack()
        for character in expression:
            if is_operand(character):
                stack.push(character)
            elif character == ' ':
                continue
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.push(f'({operand_1}{character}{operand_2})')
        
        return stack.joinWith()
    
    @staticmethod
    def prefixToInfix(expression: str) -> str:
        stack = Stack()
        for char in expression[::-1]:
            if not is_operator(char):
                stack.push(char)
            elif char == ' ':
                continue
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.push(f'({operand1}{char}{operand2})')
        return stack.pop()
    
    @staticmethod
    def postfixToPrefix(expression: str) -> str:
        infix = Stack.postfixToInfix(expression)
        return Stack.infixToPrefix(infix)
    
    @staticmethod
    def prefixToPostfix(expression: str) -> str:
        infix = Stack.prefixToInfix(expression)
        return Stack.infixToPostfix(infix)
    
    ROMAN_VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ROMAN_PAIRS = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    
    @staticmethod
    def resolveFromRomanNumber(number_expression: str) -> int:
        stack: Stack[int] = Stack()

        for numeral in number_expression:
            value = Stack.ROMAN_VALUES[numeral]

            if not stack.isEmpty and value > stack.peek:
                last = stack.pop()
                stack.push(value - last)
            else:
                stack.push(value)
        
        return stack.sum
    
    @staticmethod
    def convertToRomanNumber(number: int) -> str:
        stack: Stack[str] = Stack()

        for roman, val in Stack.ROMAN_PAIRS:
            while number >= val:
                stack.push(roman)
                number -= val
        
        return stack.joinWith()

# infix, postfix, prefix
def operator_precedence(op: str) -> int:
    if op in "+-":
        return 1
    if op in "*/%//":
        return 2
    if op == '^**':
        return 3
    return 0

def is_left_associative(op: str) -> bool:
    if op == '^' or op == "**":
        return False  # '^' is right associative
    return True 

def is_operator(c: str) -> bool:
    return c in ['+', '-', '*', '/', '^', '%', '**', '//']

def is_operand(c: str) -> bool:
    return c.isalpha() or c.isdigit()