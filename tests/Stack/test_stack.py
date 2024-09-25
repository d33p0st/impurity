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

def test_sum():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    assert stack.sum == 10

    stack.push("hehe")
    
    try:
        sum = stack.sum
    except StackError:
        assert True

def test_join():
    stack = Stack()
    stack.push(1)
    stack.push("23")
    stack.push(4)

    assert stack.joinWith('') == '1234'

def test_infixToPrefix():
    assert Stack.infixToPrefix("A+B*(C-D)") == "+A*B-CD"

def test_infixToPostfix():
    assert Stack.infixToPostfix("A+B*(C-D)") == "ABCD-*+"

def test_postfixToInfix():
    assert Stack.postfixToInfix("ABCD-*+") == "(A+(B*(C-D)))"

def test_prefixToInfix():
    assert Stack.prefixToInfix("+A*B-CD") == "(A+(B*(C-D)))"

def test_postfixToPrefix():
    assert Stack.postfixToPrefix("ABCD-*+") == "+A*B-CD"

def test_prefixToPostfix():
    assert Stack.prefixToPostfix("+A*B-CD") ==  "ABCD-*+"

def test_resolveRomanNumber():
    assert Stack.resolveRomanNumber("MXCVII") == 1097

def test_generateRomanNumber():
    assert Stack.generateRomanNumber(1097) == "MXCVII"