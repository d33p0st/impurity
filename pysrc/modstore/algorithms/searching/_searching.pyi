from typing import Iterable, Type, TypeVar, Callable, Union, Any

T = TypeVar('T', int, str, float)
CALLABLE = TypeVar('CALLABLE', bound=Callable)

def determine_type(iterable: Iterable[T]) -> Union[Type, None]:
    """`Determine type of elements in a iterable.`"""
    ...

def int_only(method: CALLABLE) -> CALLABLE:
    """`Search Object and Search Class Helper Decorator for performing internal class Checks`"""
    ...

def search_consistency(method: CALLABLE) -> CALLABLE:
    """`Search Object Class Helper Decorator for performing internal class checks.`"""
    ...

class Search:
    """`Search Class containing all search algorithms (static)`"""
    def __init__(self) -> None:
        """`This class is not meant to be init. This will raise NotImplementedError.`""" 
        ...
    
    @staticmethod
    def linear(iterable: Iterable[T], target: T) -> int: ...
    @staticmethod
    def sentinel_linear(iterable: Iterable[T], target: T) -> int: ...
    @staticmethod
    def binary(iterable: Iterable[T], target: T) -> int: ...
    @staticmethod
    def meta_binary(iterable: Iterable[T], target: T, high: int, low: int) -> int: ...
    @staticmethod
    def ternary(iterable: Iterable[T], target: T, high: int, low: int) -> int: ...
    @staticmethod
    def jump(iterable: Iterable[T], target: T) -> int: ...
    @staticmethod
    @int_only
    def interpolation(iterable: Iterable[int], target: int) -> int: ...
    @staticmethod
    def exponential(iterable: Iterable[T], target: T) -> int: ...
    @staticmethod
    def fibonacci(iterable: Iterable[T], target: T) -> int: ...
    @staticmethod
    def ubiquitous_binary(iterable: Iterable[T], target: T) -> int: ...

class SearchObject:
    """`Object where the search will be performed.`"""
    def __init__(self, iterable: Union[Iterable[T], None], target: Union[Any, None] = None, permit_objects: bool = False) -> None:
        """`Create the Search Object`
        
        #### Parameters
        - **`iterable`**: Could be a list or tuple. Tuple will be typecasted to list. Iterable should
        have same type of elements. If usage of an Iterable with mixed elements is needed, set `permit_objects`
        parameter to `True`.

        - **`target`**: The target element to find. Should have the same type as the elements of the Iterable.
        In case of mixed elements in the Iterable, target can be of any type.

        - **`permit_objects`**: permits mixed elements in the Iterable. (`Caution`: might generate errors.)

        #### Example:

        ```python
        >>> from modstore.algorithms.searching import SearchObject
        >>> so = SearchObject() # empty object, iterable and target needs to be set.
        >>> so2 = SearchObject([1, 2, 3, 4, 5, 6, 7, 10], target=6)
        >>> so2.binary # perform binary search
        5
        ```
        """
        ...
    
    @property
    def iterable(self) -> Union[Iterable[T], None]:
        """`Current Iterable`"""
        ...
    
    @iterable.setter
    def iterable(self, value: Iterable[T]) -> None: ...
    @iterable.deleter
    def iterable(self) -> None: ...

    @property
    def target(self) -> Union[Any, None]:
        """`Current Target`"""
        ...
    
    @iterable.setter
    def target(self, value: Any) -> None: ...
    @iterable.deleter
    def target(self) -> None: ...

    @property
    @search_consistency
    def linear(self) -> int:
        """`Perform Linear Search on the object.`
        
        Returns the index of the element if found else -1.
        """
        ...
    
    @property
    @search_consistency
    def sentinel_linear(self) -> int:
        """`Performs Sentinel Linear Search on the object.`
        
        Returns the index of the element if found else -1.
        """
        ...
    
    @property
    @search_consistency
    def binary(self) -> int:
        """`Performs Binary search on the object.`
        
        `Caution`: the iterable needs to be a sorted iterable.

        Returns the index of the element if found else -1.
        """
        ...
    
    @search_consistency
    def meta_binary(self, high: int, low: int) -> int:
        """`Performs a recursive one-sided binary search on the object to find the target element`
        
        `Caution`: the iterable needs to be a sorted iterable.

        Returns the index of the element if found else -1.
        """
        ...
    
    @search_consistency
    def ternary(self, high: int, low: int) -> int:
        """`Performs a ternary search on the object to find the target element`
        
        `Caution`: the iterable needs to be a sorted iterable.

        Returns the index of the element if found else -1.
        """
        ...
    
    @property
    @search_consistency
    def jump(self) -> int:
        """`Performs a jump search on the object to find the target element`
        
        `Caution`: the iterable needs to be a sorted iterable.

        Returns the index of the element if found else -1.
        """
        ...
    
    @property
    @search_consistency
    @int_only
    def interpolation(self) -> int:
        """`Performs an interpolation search on the object to find the target element.`
        
        `Caution`: The iterable should be sorted and uniformly distributed.

        Returns the index of the element if found else -1.
        """
        ...
    
    @property
    @search_consistency
    def exponential(self) -> int:
        """`Performs an exponential search on the object to find the target element.`
        
        `Caution`: the iterable needs to be sorted.

        Returns the index of the element if found else -1.
        """
        ...
    
    @property
    @search_consistency
    def fibonacci(self) -> int:
        """`Performs a fibonacci search on the the object to find the target.`
        
        `Caution`: the iterable needs to be sorted.

        Returns the index of the element if found else -1.
        """
        ...
    
    @property
    @search_consistency
    def ubiquitous_binary(self) -> int:
        """`Performs an ubiquitous binary search on the object to find the 
        smallest index of the target element.`
        
        `Caution`: the iterable needs to be sorted.

        Returns the index of the element if found else -1.
        """
        ...