from typing import Type, Union, Any, Literal, Callable, TypeVar, Generic, List as basicList, Tuple
from itertools import chain, combinations
from collections import Counter, defaultdict

from .stack import Stack, StackOverFlow
from ..exceptions import TypeCastError

T = TypeVar('T')

class List(list, Generic[T]):

    """`Modded List Class`"""
    def __str__(self) -> str:
        """`Return str(self)`"""
        return super().__str__()
    
    def __repr__(self) -> str:
        """`Return repr(self)`"""
        return super().__repr__()
    
    def __init__(self, create_from: Union[basicList[Any], 'List'] = []) -> None:
        """`Create a Modded list or List in general`
        
        ### Params
        - `create_from`: Create a Modded List from a given list or another Modded List.
        It is an optional Parameter and if kept empty, will create an
        empty Modded List.
        """
        for value in create_from:
            super().append(value)
    
    def fillByInput(self, splitby: Union[str, None] = ' ', typecast: Type = int, prompt: Union[str, None] = None) -> None:
        """`Reads from the command-line and splits the data based on 'splitby' parameter and typecasts the values if needed into
        given type. Finally, appends to the current List.`

        ### Params
        - `splitby`: pattern or str by which the input from the stdin will be split to create a list.
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
        # split the input data based on `splitby`
        read_data = input('' if prompt is None else prompt).split(splitby) if splitby != '' else list(input('' if prompt is None else prompt))

        # if data is valid, input it to inner
        for part in read_data:
            if part:
                try:
                    super().append(typecast(part) if type(part) != typecast else part)
                except Exception as e:
                    raise TypeCastError(f"Error while TypeCasting to {typecast}: {e}")
    
    def fillByString(self, string: str, splitby: Union[str, None] = ' ', typecast: Type = int) -> None:
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
        # split the string based on `splitby`
        data = string.split(splitby) if splitby != '' else list(string)

        # if data is valid, input it to inner
        for part in data:
            if part:
                try:
                    super().append(typecast(part) if type(part) != typecast else part)
                except Exception as e:
                    raise TypeCastError(f"Error while TypeCasting to {typecast}: {e}")
    
    @property
    def length(self) -> int:
        """`Length of the string.`"""
        return super().__len__()
    
    @property
    def convertToStack(self) -> Stack:
        """`Returns a 'modstore.python.Stack' type created from the current List`
        
        Returns a Stack
        """
        stack = Stack()
        for value in super().__iter__():
            stack.push(value)
        return stack
    
    def convertToStackWithCapacity(self, capacity: Union[int, None] = None) -> Stack:
        """`Returns a 'modstore.python.Stack' type with capacity of given value from the current List`
        
        ### Params
        - `capacity`: If it is set to None, capacity is `infinity`, else given `int` value.

        Returns a Stack. Raises ValueError if capacity is less than the current List length.
        """
        stack = Stack(capacity=capacity)
        for value in super().__iter__():
            try:
                stack.push(value=value)
            except StackOverFlow:
                raise ValueError(f"Failed to create stack with capacity({capacity}). Current List length is {self.length}. OverFlow condition.")
        return stack
    
    def rotate(self, k: int = 1, times: int = 1, from_: Literal['Front', 'Back'] = 'Front') -> 'List':
        """`Returns a rotated list based on given params`

        **`NOTE:`** This wont affect the original List, it will rotate and return a new List.
        
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
        newobj = self[:]
        times = times % self.length
        while times > 0:
            newK = k % self.length
            # Goes From front to Back
            if from_ == 'Front':
                newobj[:] = newobj[newK:] + newobj[:newK]
            else:
                newobj[:] = newobj[-newK:] + newobj[:-newK]
            times -= 1
        
        return List(newobj)
    
    def chunk(self, size: int = 2) -> 'List':
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

        `NOTE:` This does not modfy the current List.
        """
        return List([self[i:i+size] for i in range(0, self.length, size)])
    
    @property
    def flatten(self) -> 'List':
        """`Returns flattened version of the List`

        ### Example Usage
        ```
        >>> from modstore.python import List
        >>> somelist = List([[1, 2], [3, 4], [5, 6]])
        >>> flattened_list = somelist.flatten
        # flattened_list will be [1, 2, 3, 4, 5, 6]
        ```
        
        `NOTE:` does not modify current list, instead returns a flattened version. 
        """
        return List(chain.from_iterable(i if isinstance(i, list) else [i] for i in self))
    
    @property
    def unique(self) -> 'List':
        """`Returns a List of only unique Elements
        
        `NOTE`: The order of the elements is maintained.
        `"""
        seen = set()
        return List(x for x in self if not (x in seen or seen.add(x)))

    def filter(self, type: Type) -> 'List':
        """`Returns a List with only given types`
        
        `For Example`: There is a list, say, `[1, 2, 3, "abc", "xyz", 5, 10, "hello"]`
        and you want to filter out all the strings as a list.
        """
        return List(x for x in self if isinstance(x, type))
    
    def interleave(self, *Lists: Union['List', list]) -> 'List':
        """`Interleave the current list with other lists.`
        
        `NOTE`: This does not modify the current list.
        """
        return List(chain.from_iterable(zip(self, *Lists)))
    
    def work(self, func: Callable, store_elements: bool = False) -> 'List':
        """`Apply a function to each element in the list and return a new List.`
        
        ### Params
        - `func`: Any Function that takes one input and returns one input. Input type depends on what the
        current list is made of and subjective.
        - `store_elements`: set it to True if the callable function returns bool and you want to store values that returns True.
        """
        return List(func(x) for x in self) if not store_elements else List(x for x in self if func(x))
    
    @property
    def counter(self) -> dict:
        """`Returns a dict whose keys are the list elements and values contain their counts`"""
        return dict(Counter(self))
    
    @property
    def remove_duplicates(self) -> None:
        """`Remove Duplicates in place.`"""
        seen = set()
        self[:] = [x for x in self if not (x in seen or seen.add(x))]
    
    def swap(self, i: int, j: int):
        """`Swap two indexes.`
        
        Make sure the indexes exist, else raises IndexError.
        """
        self[i], self[j] = self[j], self[i]
    
    def partition(self, predicate: Callable) -> Tuple['List', 'List']:
        """`Partition the List based on some function.`
        
        ### Params
        - `predicate`: A callable function that takes values according to the type stored in the current List
        and returns bool.

        `NOTE`: Returns the List that returns True for `predicate` fist.

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
        return List(x for x in self if predicate(x)), List(x for x in self if not predicate(x))

    def combinations(self, n: int) -> 'List':
        """`Returns a combination of all elements.`
        
        Similar to `itertools.combinations`
        """
        return List(combinations(self, n))
    
    @property
    def reverse(self) -> None:
        """`In Place reverse`"""
        self[:] = self[::-1]
    
    @property
    def isPalindrome(self) -> bool:
        """`Returns True if palindrome else False`"""
        return self[:] == self[::-1]

    @property
    def group_anagrams(self) -> 'List[str]':
        """`Returns a List of anagrams where anagrams of same word are grouped together.`"""
        data = defaultdict(List)

        for x in self:
            sorted_ = ''.join(sorted(x, key=lambda x: ord(x)))
            data[sorted_].append(x)
        
        return List(data.values())
    
    def merge_sorted(self, other_list: Union[list, 'List'], key = None) -> 'List':
        """`Merge two arrays and sort it.`"""
        return List(sorted(self + other_list, key=key))