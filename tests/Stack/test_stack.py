from modstore.python import Stack, List
from modstore.exceptions import StackError

def test_Stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    garbage = stack.pop
    stack.push(2)
    stack.push(3)

    assert stack.peek == 3
    assert garbage == 2
    assert stack == Stack([1, 2, 3])
    assert stack == Stack(List([1, 2, 3]))
    assert stack == Stack({1: "", 2: "", 3: ""})

def test_errors():
    stack = Stack([1, 2, 3, 4, 5])

    try:
        a = stack[0]
    except StackError:
        assert True
    
    try:
        del stack[0]
    except StackError:
        assert True
    
    try:
        stack[0] = 2
    except StackError:
        assert True