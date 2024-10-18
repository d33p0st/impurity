from modstore.python import List, Stack

def test_creation():
    """`Test List Creation`"""
    list1 = List()
    
    list1.append(1)
    list1.append(2)

    list2 = List([1, 2])
    list3 = List(list2)

    assert list1 == list2
    assert list2 == list3

def test_flatten():
    """`Test List Flatten Ability`"""
    list = List([[1, 2], [3, 4], [5, 6]])

    assert list.flatten == List([1, 2, 3, 4, 5, 6])

def test_chunk():
    """`Test List Chunk Ability`"""
    list = List([1, 2, 3, 4, 5, 6])

    assert list.chunk() == List([[1, 2], [3, 4], [5, 6]])
    assert list.chunk(7) == List([[1, 2, 3 ,4 ,5 ,6]])

def test_unique():
    """`Test unique property of List`"""
    list = List([1, 1, 1, 1, 33, 44, 33, 55, 66, 77, 99, 99])
    assert list.unique == List([1, 33, 44, 55, 66, 77, 99])

def test_rotate():
    """`Check the Rotate ability of List`"""
    list = List([1, 2, 3, 4, 5])
    
    assert list.rotate(1, 2) == List([3, 4, 5, 1, 2])
    assert list.rotate(1, 2, 'Back') == List([4, 5, 1, 2, 3])

def test_checkStack():
    """`Check conversion to Stack`"""
    list = List([1, 2, 3, 4, 5])

    stack = list.convertToStack

    assert type(stack) == Stack
    assert stack.peek == 5
    assert stack.capacity == float('inf')
    assert stack.isEmpty == False

    stack = list.convertToStackWithCapacity(10)

    assert type(stack) == Stack
    assert stack.peek == 5
    assert stack.capacity == 10
    assert stack.isEmpty == False

    try:
        stack = list.convertToStackWithCapacity(3)
    except ValueError:
        assert True

def test_filter():
    list = List([1, 2, "abc", "xyz", "23", 45])

    assert list.filter(str) == List(["abc", "xyz", "23"])
    assert list.filter(int) == List([1, 2, 45])

def test_interleave():
    list = List([1, 2, 3, 4 ,5])

    assert list.interleave([10, 20, 30, 40, 50]) == List([1, 10, 2, 20, 3, 30, 4, 40, 5, 50])
    assert list.interleave([10, 20, 30], [70, 80], [100, 300]) == List([1, 10, 70, 100, 2, 20, 80, 300, 3, 30, 4, 5])

def test_work():
    def even(x: int) -> bool:
        return x%2 == 0
    
    list = List([1, 2, 3, 4, 5, 6, 7])
    assert list.work(even) == List([False, True, False, True, False, True, False])
    assert list.work(even, True) == List([2, 4, 6])

def test_counter():
    list = List([1, 2, 2, 3, 4, 5, 5])
    assert list.counter == {1: 1, 2: 2, 3: 1, 4: 1, 5: 2}

def test_remove_duplicates():
    list = List([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3])
    list.remove_duplicates
    assert list == List([1, 2, 3])

def test_swap():
    list = List([1, 2, 2, 3, 4, 5, 6])
    list.swap(0, len(list) - 1)

    assert list == List([6, 2, 2, 3, 4, 5, 1])

def test_partition():
    def even(x: int) -> bool:
        return x%2 == 0
    
    list = List([1, 2, 3 ,4, 5, 6, 7])

    a, b = list.partition(even)

    assert a == List([2, 4, 6])
    assert b == List([1, 3, 5, 7])

def test_combinations():
    from itertools import combinations

    list = List([1, 2, 3, 4, 5])

    assert list.combinations(2) == List(combinations(list, 2))

def test_reverse():
    list = List([1, 2, 3, 4, 5, 6])
    list.reverse

    assert list == List([6, 5, 4, 3, 2, 1])

def test_isPalindrome():
    list1 = List([1, 2, 1])
    list2 = List([1, 1, 2])

    assert list1.isPalindrome == True
    assert list2.isPalindrome == False

def test_group_anagrams():
    list = List(['abc', 'bca', 'ate', 'eat', 'tea'])
    anagrams = list.group_anagrams

    assert ['abc', 'bca'] in anagrams
    assert ['ate', 'eat', 'tea'] in anagrams

def test_merge_sorted():
    list = List([1, 2, 3, 4])
    assert list.merge_sorted([2, 6, 1, 3], key=lambda x: x) == List([1, 1, 2, 2, 3, 3, 4, 6])