from typing import Iterable, Any, Callable, TypeVar, Union, Tuple, List as basicList
from ...python import List
from functools import _Wrapped

T = TypeVar('T', str, int, float)
CALLABLE = TypeVar('CALLABLE', bound=Callable)

def iis(method: CALLABLE) -> CALLABLE:
    """`Internal Iterable Suport Wrapper.`
    
    Checks if the `iterable` property is set or not.
    Raises `IterableNotSet` Error if not set.
    
    Checks if the `iterable` has unsupported types.
    Raises `IterableHasUnsupportedTypeValues`.
    """
    ...

def merge(left: Union[basicList[T], List[T]], right: Union[basicList[T], List[T]], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> basicList[T]:
    """`Merge Two sorted lists (supports modstore.python.list.List)`"""
    ...

def heapify(array: basicList[T]):
    """`Transform list into a heap, in-place, in O(len(heap)) time.`"""
    ...

def is_sorted(arr: Union[basicList[T], List[T]], key: Callable[[T], Any], reverse: bool) -> bool:
    """`Checks if a list is sorted.`"""
    ...

def merge_3(left: Union[basicList[T], List[T]], middle: Union[basicList[T], List[T]], right: Union[basicList[T], List[T]], key: Callable[[T], Any], reverse: bool) -> basicList[T]:
    """`Merge 3 sorted Lists`"""
    ...

class Sort:
    """`Sort Class containing all Sort Methods (static)`"""
    def __init__(self) -> None:
        """`This is not meant to be called and will generate NotImplementedError`"""
        ...
    
    @staticmethod
    def _counting_sort_for_radix(array: Iterable[int], exp: int) -> basicList[int]:
        """
        Helper function to perform counting sort based on digit represented by exp.
        """
        ...
    
    @staticmethod
    def selection_sort(iterable: Iterable[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def bubble_sort(iterable: Iterable[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def insertion_sort(iterable: Iterable[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def merge_sort(iterable: Iterable[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def quick_sort(iterable: Iterable[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def heap_sort(array: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def counting_sort(iterable: Iterable[int], reverse: bool = False) -> List[int]: ...
    @staticmethod
    def radix_sort(array: Iterable[int], reverse: bool = False) -> List[int]: ...
    @staticmethod
    def bucket_sort(array: Iterable[int], key: Callable[[int], float] = lambda x: x, reverse: bool = False) -> List[int]: ...
    @staticmethod
    def tim_sort(array: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def bingo_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def shell_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def comb_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def pigeonhole_sort(iterable: Iterable[int], key: Callable[[int], int] = lambda x: x, reverse: bool = False) -> List[int]: ...
    @staticmethod
    def cycle_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def cocktail_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def strand_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def sleep_sort(iterable: Iterable[int], key: Callable[[int], float] = lambda x: x, reverse: bool = False) -> List[int]: ...
    @staticmethod
    def pancake_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def bogo_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def gnome_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def stooge_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def tag_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> Tuple[List[T], List[int]]: ...
    @staticmethod
    def brick_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...
    @staticmethod
    def three_way_merge_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]: ...

class SortObject:
    """`Object to be sorted.`"""
    def __init__(self, iterable: Union[Iterable[T], None] = None, key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> None:
        """`Create a SortObject to use different sorting algorithms on.`
        
        #### Params
        - **iterable**: Any Iterable [list, tuple] (supports `modstore.python.list.List`) or None. Default is None (so that an empty `SortObject` can be created. In this case, the `iterable` property
        needs to be set explicitly, else will raise `IterableNotSet` Exception).

        - **key**: Any function to pass the element of the iterable as parameter and get the key as result.

        - **reverse**: If to return the reverse.

        #### Example
        ```python
        >>> from modstore.algorithms.sorting import SortObject
        >>> so = SortObject()
        >>> so2 = SortObject([3, 1, 5, 2, 4])
        ```
        """
        ...
    
    @property
    def iterable(self) -> Union[Iterable[T], None]:
        """`Property: Returns Current Iterable`"""
        ...
    
    @iterable.setter
    def iterable(self, value: Iterable[T]) -> None: ...
    @iterable.deleter
    def iterable(self) -> None: ...
    
    @property
    def key(self) -> Callable[[T], Any]:
        """`Property: Returns Current Key`"""
        ...
    
    @key.setter
    def key(self, value: Callable[[T], Any]) -> None: ...
    @key.deleter
    def key(self) -> None: ...
    
    @property
    def reverse(self) -> bool:
        """`Property: Returns Current Reverse Status (bool)`"""
        ...
    
    @reverse.setter
    def reverse(self, value: bool) -> None: ...
    @reverse.deleter
    def reverse(self) -> None: ...

    @property
    @iis
    def selection_sort(self) -> List[T]:
        """
        `Selection Sort Algorithm`

        The `selection sort` algorithm divides the array into a sorted and unsorted part.
        It repeatedly selects the smallest (or largest) element from the unsorted part and
        swaps it with the first element of the unsorted part, expanding the sorted portion.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `List[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.selection_sort
        [1, 2, 3, 4, 5]
        ```
        """
        ...
    
    @property
    @iis
    def bubble_sort(self) -> List[T]:
        """
        `Bubble Sort Algorithm`

        `Bubble sort` repeatedly steps through the list, compares adjacent items,
        and swaps them if they are in the wrong order. This process repeats until
        no more swaps are needed.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.bubble_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def insertion_sort(self) -> List[T]:
        """
        `Insertion Sort Algorithm`

        `Insertion sort` builds the sorted list one item at a time by taking the next item
        and inserting it into its correct position among the previously sorted items.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.insertion_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def merge_sort(self) -> List[T]:
        """
        `Merge Sort Algorithm`

        `Merge sort` is a divide-and-conquer algorithm that divides the array into two halves,
        recursively sorts each half, and then merges the two sorted halves together.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.merge_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def quick_sort(self) -> List[T]:
        """
        `Quick Sort Algorithm`

        `Quick sort` is a divide-and-conquer algorithm that picks a pivot element and
        partitions the array into two sub-arrays, where elements less than the pivot
        are placed on one side and elements greater than the pivot on the other side.
        This process is repeated recursively.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.quick_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def heap_sort(self) -> List[T]:
        """
        `Heap Sort Algorithm`

        `Heap sort` first builds a max-heap (or min-heap for reverse) from the array,
        and then repeatedly removes the largest (or smallest) element from the heap,
        placing it at the end of the array, until the heap is empty.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.heap_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def counting_sort(self) -> List[T]:
        """
        `Counting Sort Algorithm`

        `Counting sort` works by counting the number of occurrences of each value in the input array,
        and then placing each value in its correct position in the output array based on its count.

        #### This method uses:
            - `array (Iterable[int])`: The array of non-negative integers to be sorted.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[int]`: The sorted List(`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.counting_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def radix_sort(self) -> List[int]:
        """
        `Radix Sort Algorithm`

        `Radix sort` processes each digit of the integers from the least significant to the most
        significant, sorting the array by each digit using a stable sorting algorithm (e.g., counting sort).

        #### This method uses:
            - `array (Iterable[int])`: The array of non-negative integers to be sorted.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[int]`: The sorted List (`modstore.python.list.List`).

        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.radix_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def bucket_sort(self) -> List[int]:
        """
        `Bucket Sort Algorithm`

        `Bucket sort` distributes elements into several buckets based on a `key` and then sorts
        each bucket individually. Finally, the sorted buckets are merged together to form the sorted array.
        This version is generalized to sort any type of values, including custom objects, by providing a `key` function.

        #### This method uses:
            - `array (Iterable[int])`: The array to be sorted (can contain any sortable type).
            - `key (Callable[[int], float], optional)`: A function that extracts a numerical value for sorting purposes. 
            Defaults to the identity function (`lambda x: x`).
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[int]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.bucket_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def bingo_sort(self) -> List[T]:
        """
        `Bingo Sort Algorithm`

        `Bingo sort` is similar to selection sort but repeatedly finds the next largest value
        and moves all elements equal to that value to the sorted part. It keeps track of the largest
        value seen so far and "bingo" is called when all elements of that value are moved.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.bingo_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def tim_sort(self) -> List[T]:
        """
        `Tim Sort Algorithm`

        `Tim sort` is a hybrid sorting algorithm derived from merge sort and insertion sort.
        It works by dividing the array into small 'runs' and sorting them using insertion sort,
        and then merging these sorted runs using a merge process similar to merge sort.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.tim_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def shell_sort(self) -> List[T]:
        """
        `Shell Sort Algorithm`

        `Shell sort` is an extension of insertion sort that allows exchanges of elements that
        are far apart. It uses a gap sequence to compare elements at increasing smaller intervals,
        improving the efficiency of the sorting process.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.shell_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def comb_sort(self) -> List[T]:
        """
        `Comb Sort Algorithm`

        `Comb sort` is an improvement over bubble sort, reducing the gap between compared
        elements gradually, starting from a large gap and shrinking it until it becomes 1,
        at which point the algorithm becomes bubble sort.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.comb_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def pigeonhole_sort(self) -> List[int]:
        """
        `Pigeonhole Sort Algorithm`

        `Pigeonhole sort` is used when the number of elements and the range of possible key values are roughly the same. 
        This version allows sorting of any type of values by providing a `key` function, which extracts an integer value 
        for placing the elements into pigeonholes.

        #### This method uses:
            - `array (Iterable[int])`: The array of any sortable type to be sorted.
            - `key (Callable[[int], int], optional)`: A function that extracts an integer value from each element 
            for sorting purposes. Defaults to the identity function (`lambda x: x`).
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[int]`: The sorted List (`modstore.python.list.List`).

        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.pigeonhole_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def cycle_sort(self) -> List[T]:
        """
        `Cycle Sort Algorithm`

        `Cycle sort` is an in-place sorting algorithm that minimizes the number of writes to
        the original array. It works by determining where each element should go and directly
        rotating the values to their correct positions.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).

        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.cycle_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def cocktail_sort(self) -> List[T]:
        """
        `Cocktail Sort Algorithm`

        `Cocktail sort`, also known as bidirectional bubble sort, sorts the array in both
        directions. It alternates between a forward and a backward pass, comparing adjacent elements
        and swapping them if they are in the wrong order.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).

        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.cocktail_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def strand_sort(self) -> List[T]:
        """
        `Strand Sort Algorithm`

        `Strand sort` is a recursive sorting algorithm that removes strands of sorted elements
        from the unsorted array and merges them into the sorted list. This continues until the
        entire array is sorted.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:

        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.strand_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def pancake_sort(self) -> List[T]:
        """
        `Pancake Sort Algorithm`

        `Pancake sort` works by repeatedly flipping the array from the top down until the largest
        unsorted element is at its correct position. The process is repeated for the remaining
        unsorted part of the array.

        #### This method uses:
            - `array (Iterable[T])`: The array to be sorted.
            - `key (Callable[[T], any], optional)`: A function that extracts a comparison key from each element. Defaults to the identity function.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[T]`: The sorted List (`modstore.python.list.List`).

        #### Example:
        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.pancake_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def sleep_sort(self) -> List[int]:
        """
        `Sleep Sort Algorithm`

        `Sleep sort` is a humorous algorithm where elements are sorted by making each element sleep for 
        an amount of time proportional to its value. This implementation uses a `key` function to determine 
        the delay for each element. Since sleep-based sorting is impractical for real-world use, this 
        version is for demonstration purposes only.

        #### This method uses:
            - `array (Iterable[int])`: The array to be sorted.
            - `key (Callable[[int], int], optional)`: A function that extracts an integer value from the element to determine the sleep duration.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[Any]`: The sorted List (`modstore.python.list.List`).

        #### Example:
        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.sleep_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def bogo_sort(self) -> List[T]:
        """
        `Bogo Sort Algorithm`

        `Bogo sort` is a highly inefficient algorithm that repeatedly shuffles the array until it is sorted.
        It is a joke algorithm that demonstrates a brute-force approach to sorting. This implementation 
        uses a `key` function to determine the sorting order.

        #### This method uses:
            - `array (Iterable[Any])`: The array to be sorted.
            - `key (Callable[[Any], Any], optional)`: A function that extracts a value from the element for sorting.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[Any]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:
        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.bogo_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def gnome_sort(self) -> List[T]:
        """
        `Gnome Sort Algorithm`

        `Gnome sort` works by comparing the current element with the previous element and swapping them 
        if they are in the wrong order, then repeating this process until the entire array is sorted.
        This version allows for sorting with a `key` function and supports both ascending and descending order.

        #### This method uses:
            - `array (Iterable[Any])`: The array to be sorted.
            - `key (Callable[[Any], Any], optional)`: A function that extracts a value from the element for sorting.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[Any]`: The sorted List (`modstore.python.list.List`).

        #### Example:
        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.gnome_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def stooge_sort(self) -> List[T]:
        """
        `Stooge Sort Algorithm`

        `Stooge sort` is a recursive sorting algorithm that sorts the first two-thirds and the last two-thirds of 
        the array, repeating the process recursively. It is highly inefficient but an interesting 
        demonstration of recursion. This implementation uses a `key` function for sorting.

        #### This method uses:
            - `array (Iterable[Any])`: The array to be sorted.
            - `key (Callable[[Any], Any], optional)`: A function that extracts a value from the element for sorting.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[Any]`: The sorted List (`modstore.python.list.List`).

        #### Example:
        ```python
        >>> obj = SortObject([5, 3, 1, 2, 4])
        >>> obj.stooge_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def tag_sort(self) -> Tuple[List[T], List[int]]:
        """
        `Tag Sort Algorithm`

        `Tag sort` pairs each element in the array with its index, sorts the elements based on a 
        `key` function, and returns both the sorted array and the original array with preserved order.
        This is useful when both sorted and original orders are needed.

        #### This method uses:
            - `array (Iterable[Any])`: The array to be sorted.
            - `key (Callable[[Any], Any], optional)`: A function that extracts a value from the element for sorting.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `tuple[list[Any], list[Any]]`: A tuple containing the sorted and the original List (`modstore.python.list.List`).

        #### Example:
        ```python
        >>> obj = SortObject([5, 2, 1, 4, 3])
        >>> obj.tag_sort
        ([1, 2, 3, 4, 5], [2, 1, 4, 3, 0])
        """
        ...
    
    @property
    @iis
    def brick_sort(self) -> List[T]:
        """
        `Brick Sort (Odd-Even Sort) Algorithm`

        `Brick sort` (also known as `Odd-Even sort`) is a parallel sorting algorithm that sorts the array 
        by repeatedly comparing and swapping adjacent elements in odd and even indexed positions. 
        This version supports a `key` function for flexible sorting.

        #### This method uses:
            - `array (Iterable[Any])`: The array to be sorted.
            - `key (Callable[[Any], Any], optional)`: A function that extracts a value from the element for sorting.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[Any]`: The sorted List (`modstore.python.list.List`).
        
        #### Example:
        ```python
        >>> obj = SortObject([5, 2, 1, 4, 3])
        >>> obj.brick_sort
        [1, 2, 3, 4, 5]
        """
        ...
    
    @property
    @iis
    def three_way_merge_sort(self) -> List[T]:
        """
        `Three-Way Merge Sort Algorithm`

        `Three-Way Merge Sort` is a variation of merge sort that divides the array into three parts instead of two, 
        recursively sorts each part, and then merges them together. This implementation uses a `key` function 
        for sorting flexibility.

        #### This method uses:
            - `array (Iterable[Any])`: The array to be sorted.
            - `key (Callable[[Any], Any], optional)`: A function that extracts a value from the element for sorting.
            - `reverse (bool, optional)`: If `True`, sorts in descending order. Defaults to `False`.

        #### Returns:
            - `list[Any]`: The sorted List (`modstore.python.list.List`).

        #### Example:
        ```python
        >>> obj = SortObject([5, 2, 1, 4, 3])
        >>> obj.three_way_merge_sort
        [1, 2, 3, 4, 5]
        """
        ...