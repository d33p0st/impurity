from typing import Generic, TypeVar, Type
from typing import SupportsIndex, Iterable, Iterator, Callable
from typing import List as basicList, Union, Literal, Tuple, Any
from typing import overload

from ..exceptions import QueueError
from .Math.constants import Infinity

T = TypeVar('T')
OtherType = TypeVar('OtherTypeThanT')

class Queue(Generic[T]):
    """Queue Data Structure.
    
    Implementation of Queue using python OOPs. Queue class can be
    used to simulate Queue type behaviour with `First-in-First-out`
    (FIFO) rule for elements.

    Supports typehints such as `Queue[int]` or `Queue[str]`.

    #### Important Note

    The Queue will act as a `Circular Queue` when given a definite
    (`int`) capacity to the constructor. On the other hand, no
    capacity provided will be considered infinite
    (`modstore.python.Math.Infinity`), and therefore will be
    implemented as a linear queue.

    For ease of use, the `Queue` class supports insertion and
    deletion from both ends (Double Ended Queue).

    #### Constructor Parameter Description

    The `capacity` parameter represents the capacity of the queue
    to be created. `None` specifies infinite, while an `int` value
    specifies a definite capacity.

    The `type` parameter can be used to specify the type of elements
    to be inserted into the Queue. This is purely optional and just
    for better typing. If different types of elements are to added,
    the `typing` module can be used.

    Example:
    ```python
    >>> from modstore.python import Queue
    >>> from typing import Union, List
    >>> queue = Queue(capacity=10, type=Union[int, str, List[str]])
    # The above line says that the Queue will have either int, str
    # or List[str] values. Hovering over (or any IDE) should show
    # Queue[int | str | List[str]] in the Queue type hint.
    ```

    Defining type hints are completely optional and added for ease
    of use and customised type hints and code suggestions. For
    example, the `enqueue` method of the the `Queue` class will
    show the parameter `value` type to whatever the type of the 
    Queue is. If it is `Queue[int]`, you will see the enqueue
    method hint as `def enqueue(self, value: int) -> bool: ...` and
    so on.

    `Additional Note:` The concept of square brackets (`'[]'`) are
    implemented, but not allowed.

    Meaning:
    ```python
    >>> queue = Queue(type=int) # Queue[int]
    >>> queue.enqueue(1)
    True
    >>> front = queue[0] # This is not allowed.
    ```

    The effort to access the queue using square brackets wont raise
    any errors related to the `Queue` class being in-accessible via
    square brackets, however, it will raise `QueueError` as accessing
    via square brackets goes against the queue rule.

    ### `Queue` Class Working Rules

    - The `Queue` will act as a Circular Queue if the capacity is set
        to be definite, otherwise, linear.
    - The `Queue` will not support accessing of elements via square
        brackets (`[]`), will raise `QueueError`.
    - The `Queue` class will support Arithmetic Operations only when
        the capacity is infinite (add, mul).
    - The `Queue` class will only support Logical Operations with
        another `Queue` or child class of `Queue` only.
    - The `Queue` supports `key in Queue` statements.
    - The `Queue` supports `for element in Queue` statements
    - The `Queue` supoorts usage of `reversed` function to iterate in
        reverse.
    - The `Queue` supports string conversion using `str` method and `repr`.
    """

    @overload
    def __init__(self) -> None:
        """Create a `Queue` object with no type hints and infinite
        capacity.
        
        NOTE: The capacity cannot be changed once defined.

        #### For detailed information on `Queue` class, see documentation or hover over `Queue` class to see docstring.
        """
        ...
    @overload
    def __init__(self, *, capacity: Union[int, Infinity]) -> None:
        """Create a `Queue` object with no type hints and user
        defined capacity, either definite or indefinite.
        
        To use infinite capacity, import `Infinity` from
        `modstore.python.Math`.

        ```python
        from modstore.python.Math import Infinity
        ```

        #### For detailed information on `Queue` class, see documentation or hover over `Queue` class to see docstring.
        """
        ...
    @overload
    def __init__(self, *, type: Type[T]) -> None:
        """Create a `Queue` object with infinite capacity and enabled
        type hinting.
        
        Example:

        ```python
        >>> from modstore import Queue
        >>> queue = Queue(type=int) # will have Queue[int] type hinting.
        ```

        #### For detailed information on `Queue` class, see documentation or hover over `Queue` class to see docstring.
        """
        ...
    @overload
    def __init__(self, *, capacity: Union[int, Infinity], type: Type[T]) -> None:
        """Create a `Queue` object with user defined capacity and enabled
        type hinting.
        
        Example:
        ```python
        >>> from modstore import Queue
        >>> from typing import Union
        >>> queue = Queue(capacity=10, type=Union[str, int])
        # Queue[str | int]
        ```

        #### For detailed information on `Queue` class, see documentation or hover over `Queue` class to see docstring.
        """
    
    @overload
    def enqueue(self, value: T) -> bool:
        """Push an element into the rear of the queue.
        
        Returns `True` if pushing is a success else `False`.
        Returns `False` if the `Queue` is full.
        """
        ...
    @overload
    def enqueue(self, value: T, *, at: Literal['front', 'rear'] = 'rear') -> bool:
        """Push an element into the queue based on `at` parameter.
        
        The `at` parameter takes only two values: `front` and `rear`, where
        the default value is 'rear'.

        Returns `True` if pushing is a success else `False`.
        Returns `False` if the `Queue` is full.
        """
        ...
    
    @overload
    def dequeue(self) -> Union[T, None]:
        """Pops an element from the front of the queue.
        
        Returns the element if success, else `None`.
        """
        ...
    @overload
    def dequeue(self, *, fro: Literal['front', 'rear'] = 'front') -> Union[T, None]:
        """Pops an element from the queue based on `fro` parameter.
        
        The `fro` parameter takes only two values: `front` and `rear`,
        where the default value is `front`.

        Returns the element if success, else `None`.
        """
        ...
    
    def error(*args: object) -> QueueError:
        """returns a QueueError object for convenience and can be used
        for generating errors.

        Example:
        ```python
        >>> from modstore import Queue
        >>> queue = Queue()
        >>> raise queue.error('Dummy Error')
        ```
        """
        ...
    
    @property
    def front(self) -> Union[T, None]:
        """The element at the front of the queue, currently."""
        ...
    
    @property
    def rear(self) -> Union[T, None]:
        """The element at the rear of the queue, currently."""
        ...
    
    @property
    def isEmpty(self) -> bool:
        """Is the queue empty?"""
        ...
    
    @property
    def isNotEmpty(self) -> bool:
        """Is the queue not empty?"""
        ...
    
    @property
    def isFull(self) -> bool:
        """Is the queue full?"""
        ...
    
    @property
    def isNotFull(self) -> bool:
        """Is the queue not full?"""
        ...
    
    @overload
    def __setitem__(self, key: SupportsIndex, value: T, /) -> None:
        """Implementation of `self[index] = value`.
        
        Blocked for `Queue` and will raise `QueueError`.
        """
        ...
    @overload
    def __setitem__(self, key: slice, value: Iterable[T], /) -> None:
        """"Implementation of `self[index_1:index_2] = [value1, value2, ...]`.
        
        Blocked for `Queue` and will raise `QueueError`.
        """
        ...
    
    @overload
    def __getitem__(self, key: SupportsIndex, /) -> T:
        """Implementation of `value = self[index]`.
        
        Blocked for `Queue` and will raise `QueueError`.
        """
        ...
    @overload
    def __getitem__(self, key: slice, /) -> 'Queue[T]':
        """Implementation of `queue_new = self[index1: index2]`.
        
        Blocked for `Queue` and will raise `QueueError`.
        """
        ...
    
    def __delitem__(self, key: Union[SupportsIndex, slice], /) -> None:
        """Implementation of `del queue[index]` and `del queue[index1: index2]`.
        
        Blocked for `Queue` and will raise `QueueError`.
        """
        ...
    
    def __contains__(self, key: object, /) -> bool:
        """Implementation of `element in queue` statement."""
        ...
    
    def __iter__(self) -> Iterator[T]:
        """Implementation of `for element in queue` statement."""
        ...
    
    def __reversed__(self) -> Iterator[T]:
        """"Implementation of `for element in reversed(queue)` statement."""
        ...
    
    def __str__(self) -> str:
        """str(queue) implementation."""
        ...
    
    def __repr__(self) -> str:
        """repr(queue) implementation."""
        ...
    
    def __len__(self) -> int:
        """len(queue) implementation. Will return current size of queue."""
        ...
    
    def __bool__(self) -> bool:
        """Implementation of `if queue:` statement."""
        ...
    
    def __queue__(self) -> basicList[T]:
        """Specific to `Queue` class. Returns the underlying list of elements."""
        ...
    
    def __add__(
            self,
            object: Union[Iterable[T], Iterable[OtherType]],
            /
    ) -> 'Queue[Union[T, OtherType]]':
        """Implementation of `queue + queue`."""
        ...
    
    def __iadd__(
            self,
            object: Union[Iterable[T], Iterable[OtherType]],
            /
    ) -> 'Queue[Union[T, OtherType]]':
        """Implementation of `queue += queue`."""
        ...
    
    def __mul__(
            self,
            object: SupportsIndex,
            /
    ) -> 'Queue[T]':
        """Implementation of `queue * (int or float)`."""
        ...
    
    def __imul__(
            self,
            object: SupportsIndex,
            /
    ) -> 'Queue[T]':
        """Implementation of `queue *= (int or float)`."""
        ...
    
    def __rmul__(
            self,
            object: SupportsIndex,
            /
    ) -> 'Queue[T]':
        """Implementation of `(int or float) * queue`."""
        ...
    
    def __eq__(self, o: object, /) -> bool:
        """Implementation of `queue == queue`."""
        ...
    
    def __ne__(self, o: object, /) -> bool:
        """Implementation of `queue != some_other_queue`."""
        ...
    
    def __gt__(self, o: object, /) -> bool:
        """Implementation of `queue > queue.`"""
        ...
    
    def __ge__(self, o: object, /) -> bool:
        """Implementation of `queue >= queue`."""
        ...
    
    def __le__(self, o: object, /) -> bool:
        """Implementation of `queue < queue`."""
        ...
    
    def __lt__(self, o: object, /) -> bool:
        """Implementation of `queue <= queue`."""
        ...
    
    def __sizeof__(self) -> int:
        """Size of object in memory, in bytes."""
        ...

class priority:
    """Pre-defined callables for `PriorityQueue`.

    #### Description

    `priority` class contains a set of pre-defined methods for
    `priority_checker` parameter of `PriorityQueue`'s constructor.
    The `priority_checker` parameter takes a callable type value which
    should be a function that takes two parameters and returns bool result.
    By default, the `priority_checker` arranges the elements in the queue in
    ascending order of their priority and therefore the default function is:

    ```python
    def default(A, B): # priority.default
        return A > B
    
    # Here, B is the priority of the element to be inserted.
    # and A is priority of some element while the queue is being iterated.
    ```

    However, this function's logic can be set to anything as long as the
    function takes two parameters and returns bool.

    By default the `priority_checker` parameter is set to be `priority.default`
    (ascending order of priority) (lower the priority value, higher the priority.)
    """

    @staticmethod
    def default(x: int, y: int) -> bool:
        """The default priority checker.
        
        This function arranges the elements based on ascending order of their
        priority.
        """
        ...
    
    @staticmethod
    def reverse(x: int, y: int) -> bool:
        """The reverse priority checker.
        
        This function arranges the elements based on descending order of their
        priority.
        """
        ...

class PriorityQueue(Queue, Generic[T]):
    """Priority Queue data structure.
    
    The elements are inserted and removed based on a priority value.
    By default, the elements are arranged in ascending order of their
    priority (lower the priority value, higher the priority).
    """

    @overload
    def __init__(self) -> None:
        """Create a Priority Queue with infinite capacity.
        
        NOTE: This definition does not support type hinting.
        """
        ...
    @overload
    def __init__(
            self,
            *,
            type: Type[T],
    ) -> None:
        """Create a Priority Queue with infinite capacity and enabled
        type hints.
        """
        ...
    @overload
    def __init__(
            self,
            *,
            capacity: Union[int, Infinity],
    ) -> None:
        """Create a Priority Queue with definite capacity.
        
        The `capacity` parameter can either take `int` value or infinite
        (`modstore.python.Math.Infinity`).

        NOTE: Type hints are disabled in this definition.
        """
        ...
    @overload
    def __init__(
            self,
            *,
            capacity: Union[int, Infinity],
            type: Type[T],
    ) -> None:
        """Create a Priority Queue with definite capacity.
        
        The `capacity` parameter can either take `int` value or infinite
        (`modstore.python.Math.Infinity`).
        
        Type hints are enabled in this definition.
        """
        ...
    @overload
    def __init__(
            self,
            *,
            capacity: Union[int, Infinity] = Infinity(),
            type: Type[T] = None,
            priority_generator: Union[Callable[[T], int], None] = None,
            priority_checker: Callable[[int, int], bool] = priority.default,
    ) -> None:
        """Create a Priority Queue with custom priority conditions.
        
        #### Parameter description
        
        `capacity` parameter defines the capacity of the queue, if left alone,
        the default value is infinity (`modstore.python.Math.Infinity`). If the
        capacity is infinite, it will act as a linear priority queue
        whereas if the capacity is definite (`int`), it will act as a circular
        priority queue for efficient management.

        `type` parameter enables type hinting in the `Queue` class and all it's
        subclasses. It can take values such as `int`, `str`, or more detailed
        types using the `typing` module.

        `priority_generator` parameter eliminates the need of providing priority
        for each element, instead, the `priority_generator` generates a priority
        for each element at runtime. It takes a `Callable[[T], int]` type value,
        which means a function that takes each element and returns a priority
        for that element.

        For example:
        ```python
        >>> def generator_1(element):
        ...     return element + 10
        # The above function takes an element and returns (element + 10)
        # (priority)
        >>> pqueue = PriorityQueue(priority_generator=generator_1)
        >>> pqueue.enqueue(10)
        # the priority will be auto-calculated to 20.
        # so the element 10 will have priority 20.
        ```

        However, even if the `priority_checker` is set, it can be bypassed,
        by providing a priority of the element.

        ```python
        >>> def generator_1(element):
        ...     return element + 10
        # The above function takes an element and returns (element + 10)
        # (priority)
        >>> pqueue = PriorityQueue(priority_generator=generator_1)
        >>> pqueue.enqueue(value = 10, priority = 40) 
        # explicitly provided priority
        ```

        The `priority_checker` parameter accepts a `Callable[[int, int], bool]`
        type value, which means a function that takes two `int` type parameters
        and returns a bool value. This `priority_checker` parameter is
        responsible for arranging the elements in specific order.

        For easy definition the `priority` class can be imported.
        ```python
        >>> from modstore import priority
        ```
        The default value of `priority_checker` parameter is `priority.default`,
        which arranges the priorities in ascending order (lower the priority
        value, higher the priority).

        For reverse order (higher the priority value, higher the priority),
        use `priority.reverse`.

        Any custom function as long as it takes two integers and returns a
        bool is supported. The first integer parameter represents the
        already inserted priorities (will be iterated one by one) while the
        second integer parameter represents the priority of the element to be
        inserted.

        The iteration will be done from the back of the queue to the front.

        For example, let us define a custom priority checker:
        ```python
        >>> def checker(x: int, y: int) -> bool:
        ...     # x is the already present priority in the pool.
        ...     # y is the current priority of the element to be inserted.
        ...     return y-10 > x

        # let us use this
        >>> pq = PriorityQueue(priority_checker=checker)
        >>> pq.enqueue(value=10, priority=100)
        True
        >>> pq.enqueue(value=20, priority=200)
        True
        >>> pq.enqueue(value=30, priority=50)
        True
        >>> pq.enqueue(value=40, priority=9)
        True
        # till now, the queue is [20, 10, 30, 40]
        >>> pq.enqueue(value=50, priority=60)
        True
        # now according to our condition,
        # while iterating from 40(end) to 20(start)
        # 60(priority of element 50) - 10 > 50 (priority of element 30) is not True.
        # therefore, the loop will exit and place it ahead of `30`
        >>> pq
        [20, 10, 30, 50, 40]
        # priorities
        # [200, 100, 50, 60, 9]
        ```
        """
        ...
    
    @overload
    def enqueue(
            self,
            value: T,
            /
    ) -> bool:
        """The element will be pushed according to the priority
        generated by `priority_generator`. If not set, priority will be
        set to `0`.
        
        Returns `True` if enqueue sucess, else `False`.
        """
        ...
    @overload
    def enqueue(
            self,
            *,
            value: T,
            priority: int,
    ) -> bool:
        """The element will be pushed according to the priority provided.
        This will bypass any `priority_generator` if set.
        
        Returns `True` if enqueue sucess, else `False`.
        """
        ...
    
    def dequeue(self) -> Union[Tuple[T, int], None]:
        """Pops an element from the queue based on higher priority.
        
        Returns a `Tuple(<element>, <priority>)` if queue is not empty,
        else `None`.
        """
        ...
    
    def __iter__(self) -> Iterator[Tuple[T, Union[int, Any]]]:
        """Implementation of `for element, priority in p_queue`"""
        ...
    
    def __reversed__(self) -> Iterator[Tuple[T, Union[int, Any]]]:
        """Implementation of `for element, priority in reversed(p_queue)`"""
        ...
    
    def __priority__(self) -> basicList[Union[int, Any]]:
        """Specific to `PriorityQueue` class.
        Returns the underlying priority book."""
        ...