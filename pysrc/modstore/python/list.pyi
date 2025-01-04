from typing import Type, Union, Any, Literal, Callable, TypeVar, Generic, List as basicList, Tuple, Iterable, Dict
from itertools import chain, combinations
from collections import Counter, defaultdict

from .stack import Stack, StackOverFlow
from ..exceptions import TypeCastError

T = TypeVar('T')
P = TypeVar('P')

class List(basicList[T], Generic[T]):
    """Modified version of built-in mutable sequence named `list`.

    If no argument is given, the constructor creates an empty `List`
    object, the argument must be an iterable if specified.
    """

    def __init__(self, create_from: Iterable[T] = []) -> None:
        """Create a `List` object.
        
        #### Parameters
        - `create_from`: Create a Modified List from a given iterable
        of elements. If not specified, creates an empty List object.
        """
        ...
    
    def fillByInput(
            self,
            splitby: Union[str, None] = None,
            typecast: Type = int,
            prompt: Union[str, None] = None,
    ) -> None:
        """`Reads from the command-line and splits the data based on 'splitby' parameter and typecasts the values if needed into
        given type. Finally, appends to the current List.`

        ### Params
        - `splitby`: pattern or str by which the input from the stdin will be split to create a list.
            By default it is `None` and it will skip any whitespace and disregard any empty strings
            from the result.
        - `prompt`: The prompt to the user.
        - `typecast`: The type of the elements to be used. By default it is `int`, which means
        if the method reads `"1 2 3 4 5"` from the stdin, it will create a List as `[1, 2, 3, 4, 5]` where
        elements are of the type `int` (here the input was `str` and it was typecasted to `int`).
        Similarly, if you want to keep it `str` and not change to `int`, set the `typecast` parameter to
        `str` and no change will be made as it is already `str`. This case will result in a List as
        `["1", "2", "3", "4", "5"]`.

        ### Errors

        Raises TypeCastError if TypeCast Fails.

        `NOTE`: this method modifies the current List and does not return anything. If the current List
        is not empty, it will append all the captured values from the `stdin` to the current List.

        `Additional NOTE`: if the split contains empty values (example: `''` or `""`), it will be ignored
        and will not be added to the List.
        """
        ...
    
    def fillByString(
            self,
            string: str,
            splitby: Union[str, None] = None,
            typecast: Type = int,
    ) -> None:
        """`Splits the given string using 'splitby' and typecasts the parts into
        'typecast' type and appends to the current List.`
        
        ### Params
        - `string`: the string which will be split.
        - `splitby`: pattern or str by which the string will be split to create a List.
        - `typecast`: The type of the elements to be used. By default it is `int`, which means
        if the method was given a string `"1 2 3 4 5"`, it will create a List as `[1, 2, 3, 4, 5]` where
        elements are of the type `int` (here the input was `str` and it was typecasted to `int`).
        Similarly, if you want to keep it `str` and not change to `int`, set the `typecast` parameter to
        `str` and no change will be made as it is already `str`. This case will result in a List as
        `["1", "2", "3", "4", "5"]`.

        ### Errors

        Raises TypeCastError if typecast fails.

        `NOTE`: this method modifies the current List and does not return anything. If the current List
        is not empty, it will append all the values from the `string` parameter parts to the current List.

        `Additional NOTE`: if the split contains empty values (example: `''` or `""`), it will be ignored
        and will not be added to the List.
        """
        ...
    
    @property
    def length(self) -> int:
        """Length of the `List`."""
        ...
    
    @property
    def convertToStack(self) -> Stack[T]:
        """`Returns a 'modstore.python.Stack' type created from the current List`
        
        Returns a Stack[T], where T is the type of elements in the List.
        """
        ...
    
    def convertToStackWithCapacity(
            self,
            capacity: Union[int, None] = None,
    ) -> Stack[T]:
        """`Returns a 'modstore.python.Stack' type with capacity of given value from the current List`
        
        ### Params
        - `capacity`: If it is set to None, capacity is `infinity`, else given `int` value.

        Returns a Stack. Raises ValueError if capacity is less than the current List length.
        """
        ...
    
    @property
    def unique(self) -> 'List[T]':
        """`A List of only unique Elements
        
        `NOTE`: The order of the elements is maintained.
        `"""
        ...
    
    @property
    def counter(self) -> Dict[T, int]:
        """`A dict whose keys are the list elements and values contain their counts`."""
        ...
    
    @property
    def remove_duplicates(self) -> None:
        """Removes duplicates in place."""
        ...
    
    @property
    def reverse(self) -> None:
        """Reverse the list in-place."""
        ...
    
    @property
    def isPalindrome(self) -> bool:
        """`Returns True if the List is a palindrome else False`"""
        ...
    
    @property
    def group_anagrams(self) -> 'List[T]':
        """`A List of anagrams where anagrams of same word are grouped together.`
        
        NOTE: This property works better if the current List is a List of `str`.
        In other cases, it might not return a result you expect.
        """
        ...
    
    def rotate(
            self,
            k: int = 1,
            times: int = 1,
            from_: Literal['Front', 'Back'] = 'Front',
    ) -> 'List[T]':
        """`Returns a rotated list based on given params`

        #### `NOTE:` This wont affect the original List, it will rotate and return a new List.
        
        ### Params
        - `k`: Number of elements to displace.
        - `times`: Number of times to rotate.
        - `from_`: Where to displace elements from. If it is set to `Front`,
        `k` elements from the front are displaced and added to the end without
        tampering the sequence. On the other hand, if it is `Back`, `k` elements
        from the back are removed and added to the front of the list.

        ### Example Usage

        ```
        >>> from modstore.python import List
        >>> some_list = List([1, 2, 3, 4, 5])
        >>> some_list.rotate(k=1, times=2) 
        # will return [3, 4, 5, 1, 2]
        
        >>> some_list.rotate(k=1, times=2, from_='Back') 
        # will return [4, 5, 1, 2, 3]
        ```
        """
        ...
    
    def chunk(self, size: int = 2) -> 'List[List[T]]':
        """`Returns a chunked List with given size.`
        
        ### Params
        - `size`: the size of the chunk.

        ### Example Usage

        ```
        >>> from modstore.python import List
        >>> some_list = List([1, 2, 3, 4, 5, 6])
        >>> chunked_list = somelist.chunk(size=2)
        # chunked_list will be [[1, 2], [3, 4], [5, 6]]
        ```

        `NOTE:` This does not modify the current List.
        """
        ...
    
    def filter(self, type: P) -> 'List[P]':
        """`Returns a List with only given types`
        
        `For Example`: There is a list, say, `[1, 2, 3, "abc", "xyz", 5, 10, "hello"]`
        and you want to filter out all the strings as a list.

        >>> list = List([1, 2, 3, 'a', 'b'])
        >>> list.filter(str)
        ['a', 'b']
        """
        ...
    
    def interleave(self, *Lists: Iterable[Any]) -> 'List[Any]':
        """`Interleave the current list with other lists or iterables.`
        
        `NOTE`: This does not modify the current list.
        """
        ...
    
    def work(
            self,
            func: Callable[[T], P],
            store_elements: bool = False
    ) -> 'List[P]':
        """`Apply a function to each element in the list and return a new List.`
        
        ### Params
        - `func`: Any Function that takes one input and returns one input. Input type depends on what the
        current list is made of and subjective.
        - `store_elements`: set it to True if the callable function returns bool and you want to store values that returns True.
        """
        ...
    
    def swap(self, i: int, j: int) -> None:
        """`Swap two indexes.`
        
        Make sure the indexes exist, else raises IndexError.
        """
        ...
    
    def partition(
            self,
            predicate: Callable[[T], bool],
    ) -> Tuple['List[T]', 'List[T]']:
        """`Partition the List based on some function.`
        
        ### Params
        - `predicate`: A callable function that takes values according to the type stored in the current List
        and returns bool.

        `NOTE`: Returns the List that returns True for `predicate` first.

        ### Usage

        ```
        >>> from modstore.python import List
        
        >>> def check(val: int) -> bool:
        ...     if val > 10:
        ...         return True
        ...     return False
        ...

        >>> some_list = List()
        >>> some_list.extend([1, 20, 3, 40, 5]) # fill the List in any way

        >>> List_of_nums_greater_than_10, List_of_nums_less_than_10 = some_list.partition(predicate=check)
        # this will return [1, 3, 5] and [20, 40].
        ```
        """
        ...
    
    def combinations(self, n: int) -> 'List[Tuple]':
        """`Returns a combination of all elements.`
        
        Similar to `itertools.combinations`
        """
        ...
    
    def merge_sorted(self, other_list: Iterable[Union[P, T]], key: Any = None) -> 'List[Union[T, P]]':
        """`Merge two arrays and sort it.`"""
        ...