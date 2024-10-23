
from typing import Iterable, Any, Callable, TypeVar, Union, Tuple, List as basicList
from functools import wraps
from ...python import List
from ...exceptions import (
    IterableNotSet,
    KeyPropertyDeleteError,
    ReversePropertyDeleteError,
    CountingSortError,
    RadixSortError,
    IterableHasUnsupportedTypeValues
)
import heapq
import threading
import time
import random

T = TypeVar('T', str, int, float)
CALLABLE = TypeVar('CALLABLE', bound=Callable)

def iis(method: CALLABLE):
    @wraps(method)
    def wrapper(self, *args, **kwargs):

        if getattr(self, 'iterable') is None:
            raise IterableNotSet("Iterable is not set for this Sort Object.")
        
        for element in getattr(self, 'iterable'):
            if not isinstance(element, str) and not isinstance(element, int) and not isinstance(element, float):
                raise IterableHasUnsupportedTypeValues(f"Iterable has unsupported value type: {type(element)}. Supported Types: [<class \'str\'>, <class \'int\'>, <class \'float\'>].")

        return method(self, *args, **kwargs)
    return wrapper

class SortObject:
    
    def __init__(self, iterable: Union[Iterable[T], None] = None, key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> None:
        self._iterable = iterable
        self._key = key
        self._ifreverse = reverse
    
    @property
    def iterable(self) -> Union[Iterable[T], None]:
        return self._iterable
    
    @iterable.setter
    def iterable(self, value: Iterable[T]) -> None:
        self._iterable = value
    
    @iterable.deleter
    def iterable(self):
        self._iterable = None
    
    @property
    def key(self) -> Callable[[T], Any]:
        return self._key

    @key.setter
    def key(self, value: Callable[[T], Any]) -> None:
        self._key = value
    
    @key.deleter
    def key(self):
        raise KeyPropertyDeleteError("Key Property cannot be deleted. It can only be changed.")
    
    @property
    def reverse(self) -> bool:
        return self._ifreverse
    
    @reverse.setter
    def reverse(self, value: bool) -> None:
        self._ifreverse = value
    
    @reverse.deleter
    def reverse(self):
        raise ReversePropertyDeleteError("Reverse Property cannot be deleted. It can only be changed.")
    
    @property
    @iis
    def selection_sort(self) -> List[T]:
        return Sort.selection_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def bubble_sort(self) -> List[T]:
        return Sort.bubble_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def insertion_sort(self) -> List[T]:
        return Sort.insertion_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def merge_sort(self) -> List[T]:
        return Sort.merge_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def quick_sort(self) -> List[T]:
        return Sort.quick_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def heap_sort(self) -> List[T]:
        return Sort.heap_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def counting_sort(self) -> List[int]:
        # check if the element is Int
        for x in self.iterable:
            if not isinstance(x, int):
                raise CountingSortError("The elements of the iterable are not int.")
        return Sort.counting_sort(self.iterable, self.reverse)
    
    @property
    @iis
    def radix_sort(self) -> List[int]:
        # check if the element is Int
        for x in self.iterable:
            if not isinstance(x, int):
                raise RadixSortError("The elements of the iterable are not int.")
        return Sort.radix_sort(self.iterable, self.reverse)
    
    @property
    @iis
    def bucket_sort(self) -> List[int]:
        return Sort.bucket_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def bingo_sort(self) -> List[T]:
        return Sort.bingo_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def tim_sort(self) -> List[T]:
        return Sort.tim_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def shell_sort(self) -> List[T]:
        return Sort.shell_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def comb_sort(self) -> List[T]:
        return Sort.comb_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def pigeonhole_sort(self) -> List[int]:
        return Sort.pigeonhole_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def cycle_sort(self) -> List[T]:
        return Sort.cycle_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def cocktail_sort(self) -> List[T]:
        return Sort.cocktail_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def strand_sort(self) -> List[T]:
        return Sort.strand_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def pancake_sort(self) -> List[T]:
        return Sort.pancake_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def sleep_sort(self) -> List[int]:
        return Sort.sleep_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def bogo_sort(self) -> List[T]:
        return Sort.bogo_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def gnome_sort(self) -> List[T]:
        return Sort.gnome_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def stooge_sort(self) -> List[T]:
        return Sort.stooge_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def tag_sort(self) -> Tuple[List[T], List[int]]:
        return Sort.tag_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def brick_sort(self) -> List[T]:
        return Sort.brick_sort(self.iterable, self.key, self.reverse)
    
    @property
    @iis
    def three_way_merge_sort(self) -> List[T]:
        return Sort.three_way_merge_sort(self.iterable, self.key, self.reverse)

def merge(left: Union[basicList[T], List[T]], right: Union[basicList[T], List[T]], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> basicList[T]:
    result: basicList[T] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if (reverse and key(left[i]) > key(right[j])) or (not reverse and key(left[i]) < key(right[j])):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heapify(array: basicList[T]):
    heapq.heapify(array)

def is_sorted(arr: Union[basicList[T], List[T]], key: Callable[[T], Any], reverse: bool) -> bool:
    for i in range(len(arr) - 1):
        if (reverse and key(arr[i]) < key(arr[i + 1])) or (not reverse and key(arr[i]) > key(arr[i + 1])):
            return False
    return True

def merge_3(left: Union[basicList[T], List[T]], middle: Union[basicList[T], List[T]], right: Union[basicList[T], List[T]], key: Callable[[T], Any], reverse: bool) -> basicList[T]:
    result: basicList[T] = []
    while left or middle or right:
        min_vals = [item for item in [left[0] if left else None, middle[0] if middle else None, right[0] if right else None] if item is not None]
        if reverse:
            next_val = max(min_vals, key=key)
        else:
            next_val = min(min_vals, key=key)

        if left and key(left[0]) == key(next_val):
            result.append(left.pop(0))
        elif middle and key(middle[0]) == key(next_val):
            result.append(middle.pop(0))
        else:
            result.append(right.pop(0))

    return result

class Sort:
    def __init__(self):
        raise NotImplementedError("This class is not meant to be init. It only contains static methods. Call Like this -> `classname.method(params)`")
    
    @staticmethod
    def selection_sort(iterable: Iterable[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> List[T]:
        array: List[T] = List(iterable)

        n = len(array)

        for i in range(n):
            selected_index = i

            for j in range(i+1, n):
                if (reverse and key(array[j]) > key(array[selected_index])) or (not reverse and key(array[j]) < key(array[selected_index])):
                    selected_index = j
            
            array[i], array[selected_index] = array[selected_index], array[i]
        
        return array

    @staticmethod
    def bubble_sort(iterable: Iterable[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr: List[T] = List(iterable)
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (reverse and key(arr[j]) < key(arr[j+1])) or (not reverse and key(arr[j]) > key(arr[j+1])):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return arr

    @staticmethod
    def insertion_sort(iterable: Iterable[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        for i in range(1, len(arr)):
            current_value = arr[i]
            j = i - 1
            while j >= 0 and ((reverse and key(arr[j]) < key(current_value)) or (not reverse and key(arr[j]) > key(current_value))):
                arr[j+1] = arr[j]
                j -= 1
            arr[j + 1] = current_value
        
        return List(arr)

    @staticmethod
    def merge_sort(iterable: Iterable[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        if len(arr) <= 1:
            return List(arr)
        mid = len(arr) // 2
        left = Sort.merge_sort(arr[:mid], key, reverse)
        right = Sort.merge_sort(arr[mid:], key, reverse)
        return List(merge(left, right, key, reverse))

    @staticmethod
    def quick_sort(iterable: Iterable[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        if len(arr) <= 1:
            return List(arr)
        pivot = arr[0]
        less = [x for x in arr[1:] if (reverse and key(x) >= key(pivot)) or (not reverse and key(x) <= key(pivot))]
        greater = [x for x in arr[1:] if (reverse and key(x) < key(pivot)) or (not reverse and key(x) > key(pivot))]
        return List(Sort.quick_sort(less, key, reverse) + [pivot] + Sort.quick_sort(greater, key, reverse))

    
    @staticmethod
    def heap_sort(array: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(array)

        def heapify_inner(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and ((not reverse and key(arr[left]) > key(arr[largest])) or (reverse and key(arr[left]) < key(arr[largest]))):
                largest = left
            if right < n and ((not reverse and key(arr[right]) > key(arr[largest])) or (reverse and key(arr[right]) < key(arr[largest]))):
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify_inner(n, largest)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify_inner(n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify_inner(i, 0)

        return List(arr)

    @staticmethod
    def counting_sort(iterable: Iterable[int], reverse: bool = False) -> List[int]:
        if not iterable:
            return List()
        
        array = list(iterable)

        max_val = max(array)
        count = [0] * (max_val + 1)
        output = [0] * len(array)

        # Count the occurrences of each element
        for num in array:
            count[num] += 1

        # Accumulate the counts to get position info
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Build the output array
        for num in reversed(array):
            output[count[num] - 1] = num
            count[num] -= 1

        if reverse:
            return List(output[::-1])
        return List(output)

    @staticmethod
    def radix_sort(array: Iterable[int], reverse: bool = False) -> List[int]:
        if not array:
            return List()

        max_val = max(array)
        exp = 1  # Start with the least significant digit

        while max_val // exp > 0:
            array = Sort._counting_sort_for_radix(array, exp)
            exp *= 10

        if reverse:
            return List(array[::-1])
        return List(array)

    @staticmethod
    def _counting_sort_for_radix(array: Iterable[int], exp: int) -> basicList[int]:
        n = len(array)
        output = [0] * n
        count = [0] * 10  # Since digits range from 0 to 9

        # Count occurrences of each digit
        for num in array:
            index = (num // exp) % 10
            count[index] += 1

        # Accumulate the counts
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        for num in reversed(array):
            index = (num // exp) % 10
            output[count[index] - 1] = num
            count[index] -= 1

        return output

    @staticmethod
    def bucket_sort(array: Iterable[int], key: Callable[[int], float] = lambda x: x, reverse: bool = False) -> List[int]:
        array = list(array)
        if not array:
            return List()

        # Apply the key function to all elements to determine the range
        values = [key(item) for item in array]
        min_value = min(values)
        max_value = max(values)
        bucket_range = (max_value - min_value) / len(array) if len(array) > 1 else 1  # To avoid division by zero

        # Create empty buckets
        buckets = [[] for _ in range(len(array))]

        # Distribute array elements into buckets based on the key value
        for item in array:
            value = key(item)
            index = int((value - min_value) / bucket_range)
            if index == len(array):  # Handle edge case where value == max_value
                index -= 1
            buckets[index].append(item)

        # Sort individual buckets and concatenate the sorted buckets
        sorted_array = []
        for bucket in buckets:
            sorted_array.extend(sorted(bucket, key=key, reverse=reverse))

        return List(sorted_array if not reverse else sorted_array[::-1])

    @staticmethod
    def tim_sort(array: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        return List(sorted(array, key=key, reverse=reverse))

    @staticmethod
    def bingo_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        if not arr:
            return List()

        highest_value = key(arr[0])
        for i in range(1, len(arr)):
            if (reverse and key(arr[i]) > highest_value) or (not reverse and key(arr[i]) < highest_value):
                highest_value = key(arr[i])

        bingo = highest_value
        next_bingo = highest_value
        i = 0

        while i < len(arr):
            found = False
            for j in range(i, len(arr)):
                if key(arr[j]) == bingo:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    found = True

            if not found:
                bingo = next_bingo
                next_bingo = key(min(arr[i:], key=key)) if not reverse else key(max(arr[i:], key=key))

        return List(arr)

    @staticmethod
    def shell_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and ((reverse and key(arr[j - gap]) < key(temp)) or (not reverse and key(arr[j - gap]) > key(temp))):
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

        return List(arr)

    @staticmethod
    def comb_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        n = len(arr)
        gap = n
        shrink_factor = 1.3
        swapped = True

        while gap > 1 or swapped:
            gap = int(gap / shrink_factor)
            if gap < 1:
                gap = 1
            swapped = False
            for i in range(n - gap):
                if (reverse and key(arr[i]) < key(arr[i + gap])) or (not reverse and key(arr[i]) > key(arr[i + gap])):
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True

        return List(arr)

    @staticmethod
    def pigeonhole_sort(iterable: Iterable[int], key: Callable[[int], int] = lambda x: x, reverse: bool = False) -> List[int]:
        array = list(iterable)
        if not array:
            return []

        # Extract key values to find min and max
        values = [key(item) for item in array]
        min_value = min(values)
        max_value = max(values)
        size = max_value - min_value + 1  # Number of pigeonholes

        # Create pigeonholes
        pigeonholes = [[] for _ in range(size)]

        # Place items in pigeonholes based on the key
        for item in array:
            pigeonholes[key(item) - min_value].append(item)

        # Reconstruct the sorted array from the pigeonholes
        sorted_array = []
        for hole in pigeonholes:
            sorted_array.extend(hole)

        return sorted_array[::-1] if reverse else sorted_array

    @staticmethod
    def cycle_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        writes = 0

        for cycle_start in range(0, len(arr) - 1):
            item = arr[cycle_start]

            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if (reverse and key(arr[i]) > key(item)) or (not reverse and key(arr[i]) < key(item)):
                    pos += 1

            if pos == cycle_start:
                continue

            while key(arr[pos]) == key(item):
                pos += 1

            arr[pos], item = item, arr[pos]
            writes += 1

            while pos != cycle_start:
                pos = cycle_start
                for i in range(cycle_start + 1, len(arr)):
                    if (reverse and key(arr[i]) > key(item)) or (not reverse and key(arr[i]) < key(item)):
                        pos += 1

                while key(arr[pos]) == key(item):
                    pos += 1

                arr[pos], item = item, arr[pos]
                writes += 1

        return List(arr)

    @staticmethod
    def cocktail_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False

            for i in range(start, end):
                if (reverse and key(arr[i]) < key(arr[i + 1])) or (not reverse and key(arr[i]) > key(arr[i + 1])):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                if (reverse and key(arr[i]) < key(arr[i + 1])) or (not reverse and key(arr[i]) > key(arr[i + 1])):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            start += 1

        return List(arr)

    @staticmethod
    def strand_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        def merge(list1, list2):
            """Merge two sorted lists into one sorted list."""
            result = []
            while list1 and list2:
                if (key(list1[0]) > key(list2[0])) if reverse else (key(list1[0]) <= key(list2[0])):
                    result.append(list1.pop(0))
                else:
                    result.append(list2.pop(0))
            result.extend(list1 if list1 else list2)
            return result

        def strand(input_list):
            """Extract a sorted subsequence (strand) from the input list."""
            sublist = [input_list.pop(0)]
            i = 0
            while i < len(input_list):
                if (key(input_list[i]) <= key(sublist[-1])) if reverse else (key(input_list[i]) >= key(sublist[-1])):
                    sublist.append(input_list.pop(i))
                else:
                    i += 1
            return sublist

        if len(iterable) < 2:
            return List(iterable)
        
        new = iterable[:]

        result = strand(new)  # Get the first strand

        while new:  # Continue until the input list is empty
            result = merge(result, strand(new))

        return List(result)

    @staticmethod
    def sleep_sort(iterable: Iterable[int], key: Callable[[int], float] = lambda x: x, reverse: bool = False) -> List[int]:
        arr = list(iterable)
        sorted_arr = []
        
        def sleep_and_add(value):
            time.sleep(key(value))
            sorted_arr.append(value)

        threads = [threading.Thread(target=sleep_and_add, args=(x,)) for x in arr]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        if reverse:
            sorted_arr.reverse()

        return List(sorted_arr)

    @staticmethod
    def pancake_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)

        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        def find_max(n):
            idx = 0
            for i in range(1, n):
                if (reverse and key(arr[i]) < key(arr[idx])) or (not reverse and key(arr[i]) > key(arr[idx])):
                    idx = i
            return idx

        curr_size = len(arr)
        while curr_size > 1:
            max_idx = find_max(curr_size)
            if max_idx != curr_size - 1:
                flip(max_idx)
                flip(curr_size - 1)
            curr_size -= 1

        return List(arr)

    @staticmethod
    def bogo_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        while not is_sorted(arr, key, reverse):
            random.shuffle(arr)
        return List(arr)

    @staticmethod
    def gnome_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        n = len(arr)
        index = 0

        while index < n:
            if index == 0 or (reverse and key(arr[index - 1]) >= key(arr[index])) or (not reverse and key(arr[index - 1]) <= key(arr[index])):
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index -= 1

        return List(arr)

    @staticmethod
    def stooge_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)

        def stooge_sort_recursive(l, h):
            if (reverse and key(arr[l]) < key(arr[h])) or (not reverse and key(arr[l]) > key(arr[h])):
                arr[l], arr[h] = arr[h], arr[l]
            if h - l + 1 > 2:
                t = (h - l + 1) // 3
                stooge_sort_recursive(l, h - t)
                stooge_sort_recursive(l + t, h)
                stooge_sort_recursive(l, h - t)

        stooge_sort_recursive(0, len(arr) - 1)
        return List(arr)

    @staticmethod
    def tag_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> Tuple[List[T], List[int]]:
        arr = list(iterable)
        tagged_arr = list(enumerate(arr))
        tagged_arr.sort(key=lambda x: key(x[1]), reverse=reverse)
        sorted_arr = [item[1] for item in tagged_arr]
        original_order = [item[0] for item in tagged_arr]
        return List(sorted_arr), List(original_order)

    @staticmethod
    def brick_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        n = len(arr)
        sorted_ = False

        while not sorted_:
            sorted_ = True
            for i in range(1, n - 1, 2):
                if (reverse and key(arr[i]) < key(arr[i + 1])) or (not reverse and key(arr[i]) > key(arr[i + 1])):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    sorted_ = False

            for i in range(0, n - 1, 2):
                if (reverse and key(arr[i]) < key(arr[i + 1])) or (not reverse and key(arr[i]) > key(arr[i + 1])):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    sorted_ = False

        return List(arr)

    @staticmethod
    def three_way_merge_sort(iterable: Iterable[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> List[T]:
        arr = list(iterable)
        if len(arr) < 2:
            return List(arr)

        third = len(arr) // 3
        left = Sort.three_way_merge_sort(arr[:third], key, reverse)
        middle = Sort.three_way_merge_sort(arr[third:2*third], key, reverse)
        right = Sort.three_way_merge_sort(arr[2*third:], key, reverse)

        return List(merge_3(left, middle, right, key, reverse))
