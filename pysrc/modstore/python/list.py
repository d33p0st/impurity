from typing import Type, Union, Any, Literal, Callable, TypeVar, Generic, List as basicList, Tuple, Iterable
from itertools import chain, combinations
from collections import Counter, defaultdict

from .stack import Stack, StackOverFlow
from ..exceptions import TypeCastError, ListError
from ..tools import classtools

T = TypeVar('T')
P = TypeVar('P')

@classtools.class_override
class List(basicList[T], Generic[T]):

    @classtools.method_override
    def __str__(self) -> str:
        """`Return str(self)`"""
        return super().__str__()
    
    @classtools.method_override
    def __repr__(self) -> str:
        """`Return repr(self)`"""
        return super().__repr__()
    
    @classtools.method_override
    def __init__(self, create_from: Iterable[T] = []) -> None:
        for value in create_from:
            super().append(value)
    
    def fillByInput(self, splitby: Union[str, None] = None, typecast: Type = int, prompt: Union[str, None] = None) -> None:
        
        # split the input data based on `splitby`
        read_data = input('' if prompt is None else prompt).split(splitby) if splitby != '' else list(input('' if prompt is None else prompt))

        # if data is valid, input it to inner
        for part in read_data:
            if part:
                try:
                    super().append(typecast(part) if type(part) != typecast else part)
                except Exception as e:
                    raise TypeCastError(f"Error while TypeCasting to {typecast}: {e}")
    
    def fillByString(self, string: str, splitby: Union[str, None] = None, typecast: Type = int) -> None:
        
        # split the string based on `splitby`
        data = string.split(splitby) if splitby != '' else list(string)

        # if data is valid, input it to inner
        for part in data:
            if part:
                try:
                    super().append(typecast(part) if type(part) != typecast else part)
                except Exception as e:
                    raise TypeCastError(f"Error while TypeCasting to {typecast}: {e}")

    def _property_error_generator(self, name: str, type: Literal['setter', 'deleter'] = 'setter') -> None:
        raise ListError(f"'{name}' property of List class cannot be " + ("set" if type == 'setter' else "deleted") + ".")

    @property
    def length(self) -> int:
        return super().__len__()
    
    @length.setter
    def length(self, value) -> None:
        return self._property_error_generator('length', 'setter')
    
    @length.deleter
    def length(self) -> None:
        return self._property_error_generator('length', 'deleter')
    
    @property
    def convertToStack(self) -> Stack[T]:
        return self.convertToStackWithCapacity()
    
    @convertToStack.setter
    def convertToStack(self, value) -> None:
        return self._property_error_generator('convertToStack', 'setter')
    
    @convertToStack.deleter
    def convertToStack(self) -> None:
        return self._property_error_generator('convertToStack', 'deleter')
    
    def convertToStackWithCapacity(self, capacity: Union[int, None] = None) -> Stack[T]:
        stack: Stack[T] = Stack(capacity=capacity)
        for value in super().__iter__():
            try:
                stack.push(value)
            except StackOverFlow:
                raise ValueError(f"Failed to create stack with capacity({capacity}). Current List length is {self.length}. OverFlow condition.")
        return stack
    
    def rotate(self, k: int = 1, times: int = 1, from_: Literal['Front', 'Back'] = 'Front') -> 'List[T]':
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
    
    def chunk(self, size: int = 2) -> 'List[List[T]]':
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
        seen = set()
        return List(x for x in self if not (x in seen or seen.add(x)))
    
    @unique.setter
    def unique(self, value) -> None:
        return self._property_error_generator('unique', 'setter')

    @unique.deleter
    def unique(self) -> None:
        return self._property_error_generator('unique', 'deleter')

    def filter(self, type: P) -> 'List[P]':
        return List(x for x in self if isinstance(x, type))
    
    def interleave(self, *Lists: Iterable[Any]) -> 'List[Any]':
        # function to check if one element is present or not.
        def check(storage_: List[Union[List, basicList, Tuple]]) -> bool:
            for l in storage_:
                if len(l) > 0:
                    return True
            
            return False
        
        new = []
        storage = List([self] + list(Lists))
        while check(storage):
            for i in range(storage.length):
                try:
                    new.append(storage[i][0])
                    storage[i] = storage[i][1:]
                except IndexError:
                    continue
        
        return new
    
    def work(self, func: Callable[[T], P], store_elements: bool = False) -> 'List[P]':
        return List(func(x) for x in self) if not store_elements else List(x for x in self if func(x))
    
    @property
    def counter(self):
        return dict(Counter(self))
    
    @counter.setter
    def counter(self, value):
        return self._property_error_generator('counter', 'setter')

    @counter.deleter
    def counter(self):
        return self._property_error_generator('counter', 'deleter')
    
    @property
    def remove_duplicates(self) -> None:
        seen = set()
        self[:] = [x for x in self if not (x in seen or seen.add(x))]
    
    @remove_duplicates.setter
    def remove_duplicates(self, value):
        return self._property_error_generator('remove_duplicates', 'setter')
    
    @remove_duplicates.deleter
    def remove_duplicates(self):
        return self._property_error_generator('remove_duplicates', 'deleter')
    
    def swap(self, i: int, j: int):
        self[i], self[j] = self[j], self[i]
    
    def partition(self, predicate: Callable[[T], bool]) -> Tuple['List[T]', 'List[T]']:
        return List(x for x in self if predicate(x)), List(x for x in self if not predicate(x))

    def combinations(self, n: int) -> 'List[Tuple]':
        return List(combinations(self, n))
    
    @property
    def reverse(self) -> None:
        """`In Place reverse`"""
        self[:] = self[::-1]
    
    @reverse.setter
    def reverse(self, value):
        return self._property_error_generator('reverse', 'setter')
    
    @reverse.deleter
    def reverse(self):
        return self._property_error_generator('reverse', 'deleter')
    
    @property
    def isPalindrome(self) -> bool:
        return self[:] == self[::-1]
    
    @isPalindrome.setter
    def isPalindrome(self, value):
        return self._property_error_generator('isPalindrome', 'setter')
    
    @isPalindrome.deleter
    def isPalindrome(self):
        return self._property_error_generator('isPalindrome', 'deleter')

    @property
    def group_anagrams(self) -> 'List[T]':
        data = defaultdict(List)

        for x in self:
            sorted_ = ''.join(sorted(str(x), key=lambda x: ord(x)))
            data[sorted_].append(x)
        
        return List(data.values())
    
    @group_anagrams.setter
    def group_anagrams(self, value):
        return self._property_error_generator('group_anagrams', 'setter')
    
    @group_anagrams.deleter
    def group_anagrams(self):
        return self._property_error_generator('group_anagrams', 'deleter')
    
    def merge_sorted(self, other_list: Iterable[Union[P, T]], key = None) -> 'List[Union[T, P]]':
        return List(sorted(self + [x for x in other_list], key=key))