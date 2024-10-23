
from typing import Iterable, TypeVar, Callable, Type, Union, Any
from functools import wraps
from ...exceptions import IterableNotSet, IterableIsNotSupported, TargetCannotBeFound, TargetNotSet, IterableHasUnsupportedTypeValues
import math

T = TypeVar('T', int, str, float)
CALLABLE = TypeVar('CALLABLE', bound=Callable)

def determine_type(iterable: Iterable[T]) -> Union[Type, None]:
    if not iterable:
        return None
    
    first_type = type(iterable[0])
    for item in iterable[1:]:
        if type(item) != first_type:
            return object
    
    return first_type

def int_only(method: CALLABLE):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # check args
        for x in args:
            if isinstance(x, Iterable):
                for value in x:
                    if not isinstance(value, int):
                        raise IterableHasUnsupportedTypeValues(f"Expected <class 'int'> values, found {type(value)}.")
        
        # check kwargs
        for name, value in kwargs:
            if isinstance(value, Iterable):
                for x in value:
                    if not isinstance(x, int):
                        raise IterableHasUnsupportedTypeValues(f"Expected <class 'int'> values, found {type(value)}.")
        
        return method(self, *args, **kwargs)
    return wrapper

def search_consistency(method: CALLABLE):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        
        # check if the iterable is set or not
        if getattr(self, 'iterable') is None:
            raise IterableNotSet("Iterable is currently set to None.")
        
        # check if the target it set or not
        if getattr(self, 'target') is None:
            raise TargetNotSet("Target is not currently set.")
        
        # check if the iterable is list or a derived form of list
        # or it could be tuple, typecast to list if it is.
        # else raise Error
        if isinstance(getattr(self, 'iterable'), tuple):
            setattr(self, 'iterable', list(getattr(self, 'iterable')))
        elif not isinstance(getattr(self, 'iterable'), list):
            raise IterableIsNotSupported("Iterable is not of the type list or its derived form. It is also not a tuple.")
        
        # check the target in case the list is not of the type object
        type_of_list = determine_type(getattr(self, 'iterable'))
        if type_of_list and type_of_list is not object:
            if type(getattr(self, 'target')) is not type_of_list:
                raise TargetCannotBeFound(f"Target cannot be found at any cost. Target type is {type(getattr(self, 'target'))} and list has {type_of_list} type elements.")
        elif type_of_list and type_of_list is object:
            if not getattr(self, '__po__'):
                raise IterableIsNotSupported("Iterable has object type elements, it might generate errors. If this is intentional, re-run with the `permit_objects` parameter set to True.")

        return method(self, *args, **kwargs)
    return wrapper

class Search:
    def __init__(self) -> None:
        raise NotImplementedError("This is class that contains only static methods and this class is not meant to be init.")
    
    @staticmethod
    def linear(iterable: Iterable[T], target: T) -> int:
        for i in range(len(iterable)):
            if iterable[i] == target:
                return i
        return -1
    
    @staticmethod
    def sentinel_linear(iterable: Iterable[T], target: T) -> int:
        n = len(iterable)
        last = iterable[-1]
        iterable[-1] = target
        i = 0
        
        while iterable[i] != target:
            i += 1
        
        iterable[-1] = last
        if i < n - 1 or iterable[-1] == target:
            return i
        return -1
    
    @staticmethod
    def binary(iterable: Iterable[T], target: T) -> int:
        low, high = 0, len(iterable) - 1
    
        while low <= high:
            mid = (low + high) // 2
            if iterable[mid] == target:
                return mid
            elif iterable[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
    
    @staticmethod
    def meta_binary(iterable: Iterable[T], target: T, high: int, low: int) -> int:
        if high < low:
            return -1
        
        if iterable[low] == target:
            return low
        
        return Search.meta_binary(iterable, target, high, low + 1)
    
    @staticmethod
    def ternary(iterable: Iterable[T], target: T, high: int, low: int) -> int:
        if high < low:
            return -1
        
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if iterable[mid1] == target:
            return mid1
        if iterable[mid2] == target:
            return mid2
        
        if target < iterable[mid1]:
            return Search.ternary(iterable, target, mid1 - 1, low)
        elif target > iterable[mid2]:
            return Search.ternary(iterable, target, high, mid2 + 1)
        else:
            return Search.ternary(iterable, target, mid2 - 1, mid1 + 1)
    
    @staticmethod
    def jump(iterable: Iterable[T], target: T) -> int:
        n = len(iterable)
        step = int(math.sqrt(n))
        prev = 0
        
        while iterable[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        
        for i in range(prev, min(step, n)):
            if iterable[i] == target:
                return i
        return -1

    @staticmethod
    @int_only
    def interpolation(iterable: Iterable[int], target: int) -> int:
        low, high = 0, len(iterable) - 1
        
        while low <= high and iterable[low] <= target <= iterable[high]:
            if low == high:
                if iterable[low] == target:
                    return low
                return -1
            
            pos = low + ((target - iterable[low]) * (high - low) // (iterable[high] - iterable[low]))
            
            if iterable[pos] == target:
                return pos
            elif iterable[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        
        return -1
    
    @staticmethod
    def exponential(iterable: Iterable[T], target: T) -> int:
        if iterable[0] == target:
            return 0
        
        n = len(iterable)
        i = 1
        
        while i < n and iterable[i] <= target:
            i *= 2
        
        return Search.binary(iterable[:min(i, n)], target)
    
    @staticmethod
    def fibonacci(iterable: Iterable[T], target: T) -> int:
        n = len(iterable)
        fib2, fib1 = 0, 1
        fib = fib2 + fib1
        
        while fib < n:
            fib2, fib1 = fib1, fib
            fib = fib2 + fib1
        
        offset = -1
        
        while fib > 1:
            i = min(offset + fib2, n - 1)
            
            if iterable[i] < target:
                fib, fib1 = fib1, fib2
                fib2 = fib - fib1
                offset = i
            elif iterable[i] > target:
                fib, fib1 = fib2, fib1 - fib2
                fib2 = fib - fib1
            else:
                return i
        
        if fib1 and iterable[offset + 1] == target:
            return offset + 1
        
        return -1
    
    @staticmethod
    def ubiquitous_binary(iterable: Iterable[T], target: T) -> int:
        low, high = 0, len(iterable) - 1
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            if iterable[mid] == target:
                result = mid
                high = mid - 1  # Continue searching in the left half to find the smallest index
            elif iterable[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return result

class SearchObject:
    def __init__(self, iterable: Union[Iterable[T], None], target: Union[Any, None] = None, permit_objects: bool = False) -> None:
        self._iterable = iterable
        self._target = target
        self.__po__ = permit_objects

    @property
    def iterable(self) -> Union[Iterable[T], None]:
        return self._iterable
    
    @iterable.setter
    def iterable(self, value: Iterable[T]) -> None:
        self._iterable = value
    
    @iterable.deleter
    def iterable(self) -> None:
        self._iterable = None
    
    @property
    def target(self) -> Union[Any, None]:
        return self._target
    
    @target.setter
    def target(self, value: Any) -> None:
        self._target = value
    
    @target.deleter
    def target(self) -> None:
        self._target = None
    
    @property
    @search_consistency
    def linear(self) -> int:
        return Search.linear(self.iterable, self.target)
    
    @property
    @search_consistency
    def sentinel_linear(self) -> int:
        return Search.sentinel_linear(self.iterable, self.target)
    
    @property
    @search_consistency
    def binary(self) -> int:
        return Search.binary(self.iterable, self.target)
    
    @search_consistency
    def meta_binary(self, high: int, low: int) -> int:
        return Search.meta_binary(self.iterable, self.target, high, low)
    
    @search_consistency
    def ternary(self, high: int, low: int) -> int:
        return Search.ternary(self.iterable, self.target, high, low)
    
    @property
    @search_consistency
    def jump(self) -> int:
        return Search.jump(self.iterable, self.target)
    
    @property
    @search_consistency
    @int_only
    def interpolation(self) -> int:
        return Search.interpolation(self.iterable, self.target)
    
    @property
    @search_consistency
    def exponential(self) -> int:
        return Search.exponential(self.iterable, self.target)
    
    @property
    @search_consistency
    def fibonacci(self) -> int:
        return Search.fibonacci(self.iterable, self.target)
    
    @property
    @search_consistency
    def ubiquitous_binary(self) -> int:
        return Search.ubiquitous_binary(self.iterable, self.target)