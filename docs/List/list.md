## List Docs

The `List` is an upgraded version of python's `list` which is an in-built data structure. `List` has a lot of extra features which will make life easy.

### Features

- **Upgrades**: `List` has a lot of upgrades which makes it the better choice. It also has built in suport for [`Stack`](/docs/Stack/stack.md).

### Usage

Let's jump onto usage.

- [Installation](#installation-if-you-havent-yet)
- [Creation](#create-a-new-list-either-empty-or-from-a-list-in-built)
- [Length](#get-length)
- [Convert to Stack](#convert-to-stack)
- [Rotate The List](#rotate-the-list-t-times-with-respect-to-k-number-of-elements-to-rotate-and-from-either-back-or-front)
- [Chunks](#chunk-the-list)
- [Flatten](#flatten-the-list)
- [Unique](#get-unique-elements)
- [Filter](#filter-elements-by-type)
- [Interleave](#interleave-two-or-more-lists-into-the-current-list)
- [Apply Function to the list](#apply-some-function-to-all-the-elements-of-the-list)
- [Counter](#count-the-occurance-of-each-element)
- [Remove Duplicates](#remove-duplicates-in-place)
- [Swap Elements](#swap-two-indexes)
- [Partition the List based on boolean function](#partition-the-list-based-on-boolean-condition)
- [Combinations](#combinations-of-the-list)
- [Reverse](#reverse-in-place)
- [Palindrome Check](#check-if-palindrome)
- [Group Anagrams](#find-and-group-the-word-anagrams)
- [Merge Sorted Lists](#merge-sorted-lists)

##### Installation (if you haven't yet)

```bash
pip install modstore
```

##### Create a new List, either empty or from a `list (in-built)`

```python
>>> somelist = List() # create an empty List

# or

>>> somelist = List([1, 2, 3, 4, 5])

# or

>>> somelist = List()
>>> somelist.append(1)
>>> somelist.append(2)
# and so on.
```

`List` inherits `list` class and has all the precursor methods in it. In addition, it has more.

```python
# create a list from user input
somelist = List()
somelist.fillByInput(
    splitby=' ', # how to split the user input
    typecast=int, # typecast from str to any you want.
) # will result in [1, 2, 3, 4, 5] if "1 2 3 4 5" was given
# as an input
```

```python
# create a list from a string.
# suppose you have a string -> "12345"
somelist = List()
somelist.fillByString(
    string="12345",
    splitby='',
    typecast=int,
)

# will result in a int list.
```

##### Get Length

```python
>>> for i in range(somelist.length):
...     # do something

# somelist is of the type `List` here.
```

##### Convert to Stack

You can either convert the `List` to a stack with infinite capacity or a definite capacity.

```python
>>> somelist = List([1, 2, 3, 4, 5])

>>> stack = somelist.converToStack # infinite capacity
>>> stack2 = somelist.convertToStackWithCapacity(10) # capacity = 10
```

##### Rotate the list `t` times with respect to `k` (number of elements to rotate) and from either `Back` or `Front`

```python
somelist = List([1, 2, 3, 4 , 5])

rotated_list = somelist.rotate(
    k=2,
    times=2,
    from_='Front'
) # this wont modify the original list
# will return [5, 1, 2, 3, 4]

# first iteration: [3, 4, 5, 1, 2]
# second iteration: [5, 1, 2, 3, 4] (final result returned)
```

##### chunk the List

```python
>>> somelist = List([1, 2, 3, 4, 5, 6])

>>> chunkedlist = somelist.chunk(2)
# will return [[1, 2], [3, 4], [5, 6]]
```

##### flatten the `List`

```python
>>> somelist = List([[1, 2], 3, 4, 5, 5, [67, 89]])

>>> flat = somelist.flatten
# will return [1, 2, 3, 4, 5, 5, 67, 89]
```

##### get unique elements

```python
>>> somelist = List([1, 1, 1, 1, 2, 3, 4 , 4, 5])

>>> unique = somelist.unique
# will return [1, 2, 3, 4, 5]
```

##### filter elements by type

```python
>>> somelist = List([1, 2, "abc", 5, 6, "b"])

>>> strings = somelist.filter(str) # ["abc", "b"]
>>> nums = somelist.filter(int) # [1, 2, 5, 6]
```

##### interleave two or more `Lists` into the current `List`

```python
# this wont modify the current list. will return a new list.
>>> somelist = List([1, 2, 3])
>>> new = somelist.interleave([4, 5, 6])
# will return [1. 4, 2, 5, 3, 6]
```

##### Apply some function to all the elements of the `List`

```python
>>> somelist = List([1, 2, 3, 4])

>>> def some_function(val: int): # here the parameter is of int
...     # type because the elements of the list are int type
...     return 2*val

>>> newlist = somelist.work(some_function)
# this will be [2, 4, 12, 16]

# Example 2
# if your function returns bool and you want to store only the true values.
>>> def even(val: int):
...     return val%2 == 0

>>> newlist2 = somelist.work(even, store_elements=True)
# will have [2, 4]
```

##### Count the occurance of each element

```python
>>> somelist = List([1, 1, 2, 3, 4 , 4])
>>> data = somelist.counter # returns a dict
# {1: 2, 2: 1, 3: 1, 4: 2}
```

##### Remove duplicates in place

```python
>>> somelist = List([1, 2, 3, 4, 5, 5, 6, 1, 2, 4, "a", "v", "a"])
>>> somelist.remove_duplicates

# now somelist will be [1, 2, 3, 4, 5, 6, "a", "v"]
```

##### swap two indexes

```python
>>> somelist = List([1, 2, 3, 4, 5])
>>> somelist.swap(0, somelist.length - 1) # swap index 0 with last element
# it will become [5, 2, 3, 4, 1]
# will throw IndexError if the index does not exist
```

##### partition the list based on boolean condition

```python
>>> somelist = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

>>> def some_function(val: int):
...     return val%2 == 0

# remember, The values that give True and returned in the first list
>>> even_nums, odd_nums = somelist.partition(some_function)

# even_nums will have [2, 4, 6, 8, 10]
# odd_nums will have [1, 3, 5, 7, 9]
```

##### combinations of the list.

```python
# this works like itertools.combinations
>>> somelist = List([1, 2, 3, 4, 5])
>>> newlist = somelist.combinations(2)
[(1, 1), (1, 2), (1, 3), ... (2, 2), (2, 3), ... (5, 5)]
```

##### Reverse in place

```python
>>> somelist = List([1, 2, 3, 4, 5])
>>> somelist.reverse
[5, 4, 3, 2, 1]
```

##### Check if palindrome

```python
>>> somelist = List([1, 2, 1])
>>> somelist.isPalindrome
True
>>> somelist = List([1, 2, 3, 4])
>>> somelist.isPalindrome
False
```

##### Find and group the word anagrams

`Anagram` of word is another word with the same number of letters and same letters.

`Example`: ate and eat are anagrams.

```python
>>> words = List(['ate', 'tea', 'eat', 'abc', 'bca', 'a'])
>>> words.group_anagrams
[['ate', 'tea', 'eat'], ['abc', 'bca'], ['a']]
```

##### Merge Sorted Lists

```python
>>> somelist = List([1, 2, 5, 6])
>>> somelist.merge_sorted([2, 4, 6])
[1, 2, 2, 4, 5, 6, 6]
```

### Install from scratch

> Make sure you have cargo installed (Rust) and VS Build Tools for C++ (for windows)

```bash
git clone https://github.com/d33p0st/modstore.git
python -m pip install --upgrade pip
pip install maturin
cd modstore
maturin develop
pip install .
```

### Issues

Feel free to submit any issues with the BlockChain Class [here](https://github.com/d33p0st/modstore/issues).

### Pull Requests

Submit pull requests [here](https://github.com/d33p0st/modstore/pulls).