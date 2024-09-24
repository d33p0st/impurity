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

def checkStack():
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