from typing import Iterable, Union, Type, List as basicList, Dict, Tuple
from typing import Generic, TypeVar, SupportsIndex, Iterator
from typing import overload

from ..exceptions.python import StackError, StackOverFlow, StackUnderFlow
from .Math.constants import Infinity

X = TypeVar('X')
Some = TypeVar('Some')

class Stack(Generic[X]):
    """Stack data structure.
    
    Implementation of stack using python OOPs. Stack class can be 
    used to simulate stack type behaviour with `Last-in-First-out`
    rule for elements.

    #### Features

    - Supports Generic Type Hints. Example: `Stack[int]` or `Stack[str]`
        just like `List[int]`, etc.
    
    - Allows only stack operations:

        - push (method)
        - pop (method)
        - peek (property)
        - top (property)
        - size (current) (property)
        - isEmpty (property)
        - isNotEmpty (property)
        - capacity (property)
        - sum (property) (Available only if `Stack` has `int` elements)
    
    - Extra Features Added for usability.

        * toList (property)
        * joinWith (method) (works like `str.join`)
        * ROMAN_VALUES (constant) (Dict[str, int])
        * ROMAN_PAIRS (constant) (ROMAN_VALUES in List[Tuple[str, int]] form.)
    
    - Pre-Defined static methods that use the `Stack` class to solve basic problems.

        * infixToPostfix
        * infixToPrefix
        * postfixToInfix
        * prefixToInfix
        * postfixToPrefix
        * prefixToPostfix
        * resolveFromRomanNumber
        * convertToRomanNumber

    The above pre-defined static methods can be used like:

    ```python
    Stack.<static-method-name>(<paramerters>)
    ```

    ### Usage `'['` and `']'` has been blocked and will raise errors.

    #### Stack can be imported in any of the following ways.

    ```python
    from modstore import Stack
    from modstore.python import Stack
    from modstore.python.stack import Stack
    ```

    #### Creating a stack object can be done in any of the following ways

    ```python
    stack = Stack() # type hints ❌.
    stack = Stack(capacity=10) # type hints ❌.

    stack: Stack[str] = Stack() # type hints ✅.

    stack = Stack(create_from=[1, 2, 3, 4]) # type hints ✅.

    stack: Stack[str] = Stack(capacity=10) # type hints ✅.
    ```
    """

    ROMAN_VALUES: Dict[str, int]
    ROMAN_PAIRS: basicList[Tuple[str, int]]

    # Skipping the internal methods and property setters and deleters
    # except capacity property.

    @property
    def top(self) -> int:
        """returns the top index.
        
        Since access through square brackets are disabled, this
        property can only be used for insights.
        """
        ...
    
    @property
    def peek(self) -> X:
        """The Top Element."""
        ...
    
    @property
    def isEmpty(self) -> bool:
        """True if the `Stack` is empty else False."""
        ...
    
    @property
    def isNotEmpty(self) -> bool:
        """True if the `Stack` is not empty else False."""
        ...
    
    @property
    def size(self) -> int:
        """Current `Stack` size."""
        ...
    
    @property
    def sum(self) -> X:
        """Arithmetic sum if all elements are `<class 'int'>` or `<class 'float'>`.
        
        If all elements are `<class 'str'>`, it is the final concatenated result.

        Else, raises `Stack Error`.
        """
        ...
    
    @property
    def toList(self) -> basicList[X]:
        """List of all stack elements."""
        ...
    
    @property
    def capacity(self) -> Union[int, Infinity]:
        """Current set `Stack` capacity."""
        ...
    
    @capacity.setter
    def capacity(self, capacity: Union[int, None]) -> None: ...
    @capacity.deleter
    def capacity(self) -> None: ...

    def append(self, object: X) -> None:
        """Forcefully add an object at the top of the stack.
        
        This ignores capacity constraints. It is ideal to use
        `push` for all add operations to the stack.
        """
        ...
    
    def push(self, object: X) -> None:
        """Adds an object at the top of the stack.
        
        If capacity is full, raises `StackOverFlow` Exception.
        """
        ...
    
    def pop(self, garbage: bool = False) -> Union[X, None]:
        """Removes and returns the element at the top of the stack,
        if `garbage` is set to `False`.
        
        `garbage` parameter is provided to safely pop the element
        from the top of the stack and dispose it off. (delete)

        For example: If the to-be-popped value is not required,
        set `garbage` to `True`

        ```python
        >>> some_element = stack.pop() # the element will be returned.
        >>> stack.pop(garbage=True) # will return nothing.
        >>> #
        ```

        To get the element at the top without removing it from the stack,
        use `peek` property.
        """
        ...
    
    def joinWith(self, sep: str = '') -> str:
        """Just like `str.join(<some-iterable>)`, this method returns
        a string which is a concatenation of the string representation
        (`str(element)`) of all the elements of the stack seperated by
        `sep` (parameter, default = `''`).

        `stack.joinWith('-')` is equivalent to `'-'.join(stack.toList)`
        """
        ...

    @staticmethod
    def infixToPostfix(expression: str) -> str:
        """Converts an infix `expression` into postfix.
        
        Removes any brackets present in the `expression`.
        For example, for `(a+b)+(c/d)` it will return `ab+cd/+`.
        """
        ...
    
    @staticmethod
    def infixToPrefix(expression: str) -> str:
        """Converts an infix `expression` into prefix.
        
        Removes any brackets present in the `expression`.
        For example, for `(a+b)`, it will return `+ab`.
        """
        ...
    
    @staticmethod
    def postfixToInfix(expression: str) -> str:
        """Converts a postfix `expression` into infix.
        
        Adds brackets in the result.
        """
        ...
    
    @staticmethod
    def prefixToInfix(expression: str) -> str:
        """Converts a prefix `expression` into infix.
        
        Adds brackets in the result.
        """
        ...
    
    @staticmethod
    def postfixToPrefix(expression: str) -> str:
        """Converts a postfix `expression` into prefix."""
        ...
    
    @staticmethod
    def prefixToPostfix(expression: str) -> str:
        """Converts a prefix `expression` into postfix."""
        ...
    
    @staticmethod
    def resolveFromRomanNumber(number_expression: str) -> int:
        """Converts a Roman Number string into its integer form."""
        ...
    
    @staticmethod
    def convertToRomanNumber(number: int) -> str:
        """Converts a `number` into Roman Number."""
        ...
    
    @overload
    def __init__(self) -> None:
        """Create an empty `Stack` object with infinite capacity."""
        ...
    @overload
    def __init__(
            self,
            *,
            create_from: Iterable[X] = [],
            capacity: Union[int, None] = None,
    ) -> None:
        """create a `Stack` object.
        
        All parameters are keyword arguments and needs to be
        passed as the same.

        `create_from`: Uses the provided iterable to make an initial
        stack

        `capacity`: If None, Inifinite capacity, else definite.
        """
        ...
    
    @overload
    def __setitem__(self, key: SupportsIndex, value: X, /) -> None:
        """Should've worked like `stack[index] = value` but is disabled
        to avoid breaking stack rules."""
        ...
    @overload
    def __setitem__(self, key: slice, value: Iterable[X], /) -> None:
        """Should've worked like `stack[i:j] = [value_1, value_2]`
        where `i` and `j` are integers and `0 <= i <= j <= len(stack)`.
        
        Disabled to avoid breaking stack rules."""
        ...
    
    @overload
    def __getitem__(self, how: SupportsIndex, /) -> X:
        """Should've worked like `x = stack[0]` but is disabled to avoid
        breaking stack rules."""
        ...
    @overload
    def __getitem__(self, how: slice, /) -> 'Stack[X]':
        """Should've worked like `x = stack[1:2]` but is disabled to
        avoid breaking stack rules."""
        ...
    
    def __delitem__(self, key: Union[SupportsIndex, slice], /) -> None:
        """Should've worked like `del stack[0]` but is disabled to avoid
        breaking stack rules."""
        ...
    
    def __contains__(self, key: object, /) -> bool:
        """Returns `key` in `self`."""
        ...
    
    def __iter__(self) -> Iterator[X]:
        """Returns an iterator over stack elements."""
        ...
    
    def __reversed__(self) -> Iterator[X]:
        """Returns a reverse iterator over stack elements."""
        ...
    
    def __str__(self) -> str:
        """Equivalent to `str(stack)`"""
        ...
    
    def __repr__(self) -> str:
        """`repr(stack)`."""
        ...
    
    def __len__(self) -> int:
        """Equivalent to `len(stack)`."""
        ...
    
    @overload
    def __add__(self, object: Union['Stack[X]', basicList[X]], /) -> 'Stack[X]':
        """Returns `self[X] + other[X]`."""
        ...
    @overload
    def __add__(self, object: Union['Stack[Some]', basicList[Some]], /) -> 'Stack[Union[X, Some]]':
        """Returns `self[X] + other[Some]`."""
        ...
    
    def __mul__(self, object: SupportsIndex, /) -> 'Stack[X]':
        """Returns `Stack[X] * n`."""
        ...
    
    def __rmul__(self, object: SupportsIndex, /) -> 'Stack[X]':
        """Returns `n * Stack[X]`."""
        ...
    
    def __iadd__(self, object: Iterable[X], /) -> 'Stack[X]':
        """Implements `self += value`."""
        ...
    
    def __imull__(self, object: SupportsIndex, /) -> 'Stack[X]':
        """Implements `self *= value`."""
        ...
    
    def __eq__(self, object: object, /) -> bool:
        """Implements `==`."""
        ...
    
    def __ne__(self, object: object, /) -> bool:
        """Implements `!=`."""
        ...
    
    def __ge__(self, object: Union['Stack[X]', basicList[X]], /) -> bool:
        """Implements `>=`."""
    ...

    def __gt__(self, object: Union['Stack[X]', basicList[X]], /) -> bool:
        """Implements `>`."""
        ...
    
    def __lt__(self, object: Union['Stack[X]', basicList[X]], /) -> bool:
        """Implements `<`."""
        ...
    
    def __le__(self, object: Union['Stack[X]', basicList[X]], /) -> bool:
        """Implements '<='."""
        ...

    def __bool__(self) -> bool:
        """Implements `if stack:` and `if not stack:`."""
        ...
    
    def __sizeof__(self) -> int:
        """Size of internal stack object (list) in memory, in bytes."""
        ...

def operator_precedence(op: str) -> int:
    """Returns 1 for `+-`, 2 for `*/%//` and 3 for `^**`"""
    ...

def is_left_associative(op: str) -> bool:
    """Except `^` and `**`, returns True."""
    ...

def is_operator(c: str) -> bool: ...
def is_operand(c: str) -> bool: ...