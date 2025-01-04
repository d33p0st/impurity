from typing import Any, Generic, TypeVar, Type
from typing import Union, Literal, SupportsIndex, Iterable, Iterator, Callable, Tuple
from typing import List as basicList
from typing import overload
from tabulate import tabulate

from ..exceptions import QueueError
from ..tools.typing import classtools
from .Math.constants import Infinity

T = TypeVar('T')
OtherType = TypeVar('OtherTypeThanT')

class Queue(Generic[T]):
    # circular queue if capacity is given
    def __init__(self, capacity: Union[int, Infinity] = Infinity(), type: Type[T] = None) -> None:
        if isinstance(capacity, Infinity):
            self._queue: basicList[T] = []
        elif isinstance(capacity, int):
            self._queue: basicList[T] = [None] * capacity
        else:
            raise QueueError("'capacity' parameter can only be `modstore.python.Math.Infinity` or `int` type.")
        
        self._capacity = capacity
        self._size = 0
        self._front = 0
        self._elemtypes = type
        return None

    def _property_error_generator(self, name: str, type: Literal['setter', 'deleter'] = 'setter') -> None:
        if type == 'setter':
            raise QueueError(f"'{name}' property of Queue cannot be set.")
        else:
            raise QueueError(f"'{name}' property of Queue cannot be deleted.")
    
    def _internal_error_generator(self, name: str, message: str) -> None:
        raise QueueError(f"[{name}] {message}")
    
    def enqueue(self, value: T, at: Literal['front', 'rear'] = 'rear') -> bool:
        # if capacity exists and it is full, return False
        if not isinstance(self._capacity, Infinity) and self._capacity == self._size:
            return False
        
        if isinstance(self._capacity, Infinity):
            # if infinite capacity, consider linear
            # front
            if at == 'front':
                # check if front-1 exists in the queue
                if self._front > 0:
                    self._front -= 1
                    self._queue[self._front] = value
                    self._size += 1
                    return True
                
                self._queue = [value] + self._queue
                self._size += 1
                return True
            else:
                # rear, linear
                # try to check if the value at queue[size] is available
                # to overwrite
                try:
                    self._queue[self._size] = value
                except IndexError: # if not, append it
                    self._queue.append(value)
                
                # increment size
                self._size += 1
                return True
        else: # finite capacity, circular queue

            if at == 'front':
                self._front = (self._front - 1) % self._capacity
                self._queue[self._front] = value
                self._size += 1
                return True
            else:
                # rear, circular
                self._queue[(self._front + self._size) % self._capacity] = value
                self._size += 1
                return True
        
    def dequeue(self, fro: Literal['front', 'rear'] = 'front') -> Union[T, None]:
        # return none if size is 0
        if self._size == 0:
            return None
        
        if isinstance(self._capacity, Infinity): # for infinite capacity
            # linear
            if fro == 'front':
                self._front += 1
                self._size -= 1
                return self._queue[self._front - 1]
            else:
                self._size -= 1
                return self._queue[self._size]
        else: # definite capacity, circular queue
            if fro == 'front':
                value = self._queue[self._front]
                self._front  = (self._front + 1) % self._capacity
                self._size -= 1
                return value
            else:
                # rear
                self._size -= 1
                return self._queue[(self._front + self._size) % self._capacity]
    
    def error(*args: object) -> QueueError:
        return QueueError(*args)

    @property
    def front(self) -> Union[T, None]:
        if self._size == 0:
            return None
        
        if isinstance(self._capacity, Infinity):
            return self._queue[self._front]
        else:
            return self._queue[self._front % self._capacity]
    
    @front.setter
    def front(self, value):
        return self._property_error_generator('front', 'setter')
    
    @front.deleter
    def front(self):
        return self._property_error_generator('front', 'deleter')
    
    @property
    def rear(self) -> Union[T, None]:
        if self._size == 0:
            return None
        
        if isinstance(self._capacity, Infinity):
            return self._queue[self._size - 1]
        else:
            return self._queue[(self._front + self._size - 1) % self._capacity]
    
    @rear.setter
    def rear(self, value):
        return self._property_error_generator('rear', 'setter')
    
    @rear.deleter
    def rear(self):
        return self._property_error_generator('rear', 'deleter')
    
    @property
    def isEmpty(self) -> bool:
        return self._size == 0

    @isEmpty.setter
    def isEmpty(self, value):
        return self._property_error_generator('isEmpty', 'setter')
    
    @isEmpty.deleter
    def isEmpty(self):
        return self._property_error_generator('isEmpty', 'deleter')
    
    @property
    def isNotEmpty(self) -> bool:
        return not self.isEmpty
    
    @isNotEmpty.setter
    def isNotEmpty(self, value):
        return self._property_error_generator('isNotEmpty', 'setter')
    
    @isNotEmpty.deleter
    def isNotEmpty(self) -> None:
        return self._property_error_generator('isNotEmpty', 'deleter')
    
    @property
    def isFull(self) -> bool:
        if isinstance(self._capacity, Infinity):
            return False
        else:
            return self._size == self._capacity
        
    @isFull.setter
    def isFull(self, value):
        return self._property_error_generator('isFull', 'setter')
    
    @isFull.deleter
    def isFull(self):
        return self._property_error_generator('isFull', 'deleter')
    
    @property
    def isNotFull(self) -> bool:
        return not self.isFull
    
    @isNotFull.setter
    def isNotFull(self, value):
        return self._property_error_generator('isNotFull', 'setter')
    
    @isNotFull.deleter
    def isNotFull(self) -> None:
        return self._property_error_generator('isNotFull', 'deleter')
    
    @overload
    def __setitem__(self, key: SupportsIndex, value: T, /) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Iterable[T], /) -> None: ...

    def __setitem__(self, key: Union[SupportsIndex, slice], value: Union[T, Iterable[T]], /) -> None:
        return self._internal_error_generator(self.__setitem__.__name__, "Queue does not support assignment via [].")
    
    @overload
    def __getitem__(self, key: SupportsIndex, /) -> T: ...
    @overload
    def __getitem__(self, key: slice, /) -> 'Queue[T]':...

    def __getitem__(self, key: Union[SupportsIndex, slice], /) -> Union[T, 'Queue[T]']:
        return self._internal_error_generator(self.__getitem__.__name__, "Queue does not support accessing of elements via [].")
    
    def __delitem__(self, key: Union[SupportsIndex, slice], /) -> None:
        return self._internal_error_generator(self.__delitem__.__name__, "Queue does not support deletion via [].")
    
    def __contains__(self, key: object, /) -> bool:
        if self.isEmpty:
            return False
        return key in iter(self)
    
    def __iter__(self) -> Iterator[T]:
        if self.isEmpty:
            return [].__iter__()
        
        index = self._front
        for _ in range(self._size):
            yield self._queue[index]
            if isinstance(self._capacity, Infinity):
                index = index + 1
            else:
                index = (index + 1) % self._capacity
    
    def __reversed__(self) -> Iterator[T]:
        if self.isEmpty:
            return [].__iter__()
        
        if isinstance(self._capacity, Infinity):
            index = self._size - 1
        else:
            index = (self._front + self._size - 1) % self._capacity
        
        for _ in range(self._size):
            yield self._queue[index]
            if isinstance(self._capacity, Infinity):
                index -= 1
            else:
                index = (index - 1 + self._capacity) % self._capacity
    
    def __str__(self) -> str:
        return str([x for x in self])
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __len__(self) -> int:
        return self._size
    
    def __bool__(self) -> bool:
        return self.isNotEmpty
    
    def __queue__(self) -> basicList[T]:
        if isinstance(self._capacity, Infinity):
            return self._queue
        else:
            return [x for x in self]
    
    def __add__(self, object: Union[Iterable[T], Iterable[OtherType]], /) -> 'Queue[Union[T, OtherType]]':
        if not isinstance(object, Iterable):
            raise QueueError('The object to be added to the queue must be an iterable.')
        if isinstance(self._capacity, Infinity):
            for elem in object:
                status = self.enqueue(elem)
                if not status:
                    raise QueueError('Cannot enqueue the values from the iterable')
        else:
            raise QueueError('Cannot add to a Queue with definite capacity.')
    
    def __iadd__(self, object: Union[Iterable[T], Iterable[OtherType]], /) -> 'Queue[Union[T, OtherType]]':
        return self.__add__(object)
    
    def __mul__(self, object: SupportsIndex, /) -> 'Queue[T]':
        if isinstance(self._capacity, Infinity):
            new = Queue(self._capacity * object, self._elemtypes)
            elements = [x for x in self].__mul__(object)
            for x in elements:
                status = new.enqueue(elements)
                if not status:
                    QueueError("Interanl Error during multiplication.")
        else:
            raise QueueError("Cannot multiply with a Queue with definite capacity.")
    
    def __imul__(self, object: SupportsIndex, /) -> 'Queue[T]':
        return self.__mul__(object)
    
    def __rmul__(self, object: SupportsIndex, /) -> 'Queue[T]':
        return self.__mul__(object)
    
    def __eq__(self, o: object, /) -> bool:
        if isinstance(o, Queue):
            return self._queue == o._queue \
                    and self._capacity == o._capacity \
                    and self._front == o._front \
                    and self._size == o._size
        else:
            return False
    
    def __ne__(self, o: object, /) -> bool:
        return not self.__eq__(object)
    
    def __gt__(self, o: object, /) -> bool:
        if isinstance(o, Queue):
            return len(self._queue) > len(o._queue) \
                    and self._capacity > o._capacity \
                    and self._size > o._size
        else:
            return False
    
    def __ge__(self, o: object, /) -> bool:
        return self > o or self == o
    
    def __le__(self, o: object, /) -> bool:
        return not self.__ge__(o)
    
    def __lt__(self, o: object, /) -> bool:
        return self.__gt__(o)
    
    def __sizeof__(self) -> int:
        return self._queue.__sizeof__() \
                + self._front.__sizeof__() \
                + self._capacity.__sizeof__() \
                + self._size.__sizeof__()

class priority:
    @staticmethod
    def default(x, y):
        return x > y
    
    @staticmethod
    def reverse(x, y):
        return y > x

@classtools.class_override
class PriorityQueue(Queue, Generic[T]):

    @classtools.method_override
    def __init__(
            self,
            capacity: Union[int, Infinity] = Infinity(),
            type: Type[T] = None,
            priority_generator: Union[Callable[[T], int], None] = None,
            priority_checker: Callable[[int, int], bool] = priority.default,
    ) -> None:
        if isinstance(capacity, Infinity):
            self._queue: basicList[T] = []
            self._priority_book: basicList[int] = []
        elif isinstance(capacity, int):
            self._queue: basicList[T] = [None] * capacity
            self._priority_book: basicList[int] = [None] * capacity
        else:
            raise QueueError("'capacity' parameter can only be `modstore.python.Math.Infinity` or `int` type.")
        
        self._capacity = capacity
        self._size = 0
        self._front = 0
        self._rear = 0
        self._elemtypes = type
        self._priority_generator = priority_generator
        self._priority_checker = priority_checker
        return None
    
    @classtools.method_override
    def enqueue(
            self,
            value: T,
            priority: Union[int, None] = None,
    ) -> bool:
        if self.isFull:
            return False
        
        if not priority:
            if not self._priority_generator:
                priority = 0
            else:
                priority = self._priority_generator(value)

        if isinstance(self._capacity, int): # for circular nature
            if self.isEmpty:
                self._queue[self._rear] = value
                self._priority_book[self._rear] = priority
                self._size += 1
                return True

            position = self._rear
            while position != (self._front - 1) % self._capacity:
                if self._priority_checker:
                    if self._priority_checker(self._priority_book[position], priority):
                        pass
                    else:
                        break
                elif self._priority_book[position] > priority:
                    pass
                else:
                    break

                next_position = (position + 1) % self._capacity
                self._queue[next_position] = self._queue[position]
                self._priority_book[next_position] = self._priority_book[position]
                position = (position - 1) % self._capacity
            
            self._queue[(position + 1) % self._capacity] = value
            self._priority_book[(position + 1) % self._capacity] = priority
            self._rear = (self._rear + 1) % self._capacity
            self._size += 1
            return True
        else:

            if self.isEmpty:
                self._queue.append(value)
                self._priority_book.append(priority)
                self._size += 1
                return True
            
            # linear
            # for i in range(len(self._queue)):
            #     if ((self._priority_checker and self._priority_checker(self._priority_book[i], priority)) or (self._priority_book[i] > priority)):
            #         self._queue.insert(i, value)
            #         self._priority_book.insert(i, priority)
            #         self._size += 1
            #         self._rear += 1
            #         return True
            
            # self._queue.append(value)
            # self._priority_book.append(priority)
            # self._size += 1
            # self._rear += 1
            # return True

            position = self._rear
            while position != (self._front - 1):
                if self._priority_checker:
                    if self._priority_checker(self._priority_book[position], priority):
                        pass
                    else:
                        break
                elif self._priority_book[position] > priority:
                    pass
                else:
                    break

                next_position = position + 1
                if len(self._queue) == next_position:
                    self._queue.append(self._queue[position])
                    self._priority_book.append(self._priority_book[position])
                else:
                    self._queue[next_position] = self._queue[position]
                    self._priority_book[next_position] = self._priority_book[position]
                position = position - 1
            
            if position + 1 == len(self._queue):
                self._queue.append(value)
                self._priority_book.append(priority)
            else:
                self._queue[position + 1] = value
                self._priority_book[position + 1] = priority
            self._size += 1
            self._rear += 1
            return True
    
    @classtools.method_override
    def dequeue(self) -> Union[Tuple[T, int], None]:
        if self.isEmpty:
            return None
        
        if isinstance(self._capacity, int):
            # circular version
            value = self._queue[self._front]
            priority = self._priority_book[self._front]

            self._queue[self._front] = None
            self._priority_book[self._front] = None
            self._front = (self._front + 1) % self._capacity
            self._size -= 1
            return value, priority
        else:
            # linear queue
            value = self._queue.pop(0)
            priority = self._priority_book.pop(0)
            self._size -= 1
            if self._rear > 0:
                self._rear -= 1

            return value, priority
    
    @classtools.method_override
    def __iter__(self) -> Iterator[Tuple[T, Union[int, Any]]]:
        if self.isEmpty:
            return [].__iter__()
        
        index = self._front
        while index != self._rear:
            if self._queue[index] is not None and self._priority_book[index] is not None:
                yield (self._queue[index], self._priority_book[index])
            if isinstance(self._capacity, Infinity):
                index = index + 1
            else:
                index = (index + 1) % self._capacity
        if self._queue[index] is not None and self._priority_book[index] is not None:
            yield (self._queue[index], self._priority_book[index])

    @classtools.method_override
    def __reversed__(self) -> Iterator[Tuple[T, Union[int, Any]]]:
        if self.isEmpty:
            return [].__iter__()
        
        if isinstance(self._capacity, Infinity):
            index = self._size - 1
        else:
            index = (self._front + self._size - 1) % self._capacity
        
        while index != self._front:
            if self._queue[index] is not None and self._priority_book[index] is not None:
                yield (self._queue[index], self._priority_book[index])
            if isinstance(self._capacity, Infinity):
                index -= 1
            else:
                index = (index - 1 + self._capacity) % self._capacity
        
        if self._queue[index] is not None and self._priority_book[index] is not None:
            yield (self._queue[index], self._priority_book[index])

    @classtools.method_override
    def __str__(self) -> str:
        elements = []

        for x, y in self:
            elements.append((x, y))
        
        if not elements:
            return "~/~"
        
        return tabulate(elements, headers=['Element', 'Priority'], tablefmt='grid')
    
    @classtools.method_override
    def __repr__(self) -> str:
        return self.__str__()
    
    @classtools.method_override
    def __contains__(self, key: object, /) -> bool:
        if self.isEmpty:
            return False
        
        return key in [x[0] for x in self]
    
    @classtools.method_override
    def __queue__(self) -> basicList[T]:
        if isinstance(self._capacity, Infinity):
            return self._queue
        else:
            return [x[0] for x in self]
    
    def __priority__(self) -> basicList[Union[int, Any]]:
        if isinstance(self._capacity, Infinity):
            return self._priority_book
        else:
            return [x[1] for x in self]
    
    @classtools.method_override
    def __add__(self, object: Union[Iterable[T], Iterable[OtherType]], /) -> 'Queue[Union[T, OtherType]]':
        raise self.error("Addition not supported in Priority Queue.")

    @classtools.method_override
    def __iadd__(self, object: Union[Iterable[T], Iterable[OtherType]], /) -> 'Queue[Union[T, OtherType]]':
        return self.__add__(object)

    @classtools.method_override
    def __mul__(self, object: SupportsIndex, /) -> 'Queue[T]':
        raise self.error("Multiplication not supported in Priority Queue.")

    @classtools.method_override
    def __imul__(self, object: SupportsIndex, /) -> 'Queue[T]':
        return self.__mul__(object)

    @classtools.method_override
    def __rmul__(self, object: SupportsIndex, /) -> 'Queue[T]':
        return self.__mul__(object)
    
    @classtools.method_override
    def __sizeof__(self) -> int:
        return self._queue.__sizeof__() \
                + self._front.__sizeof__() \
                + self._capacity.__sizeof__() \
                + self._size.__sizeof__() \
                + self._rear.__sizeof__() \
                + self._priority_book.__sizeof__() \
                + self._priority_checker.__sizeof__() \
                + self._priority_generator.__sizeof__()