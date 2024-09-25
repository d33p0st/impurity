from typing import Union, Any, Iterable, List as basicList
from ..exceptions.python import StackOverFlow, StackUnderFlow, StackError

class Stack(list):
    def __init__(self, create_from: Union[basicList[Any], Iterable] = [], capacity: Union[int, None] = None) -> None:
        for value in create_from:
            super().append(value)
        
        self._capacity = capacity
    
    def __setitem__(self, index, value):
        raise StackError("Stack does not support assignment via [].")
    
    def __getitem__(self, index):
        raise StackError("Stack does not support accessing of elements via [].")
    
    def __delitem__(self, index):
        raise StackError("Stack does not support deletion via [].")
    
    def append(self, object: Any) -> None:
        raise StackError("Use Push. Append is disabled.")
    
    @property
    def top(self) -> int:
        return super().__len__() - 1

    @property
    def pop(self) -> Any:
        """
        `Pops an element from the top.`

        Raises StackUnderFlow Exception if Stack is Empty
        """
        try:
            value = super().pop()
        except IndexError:
            raise StackUnderFlow("Stack is empty.")
        
        return value
    
    def push(self, value: Any):
        if self._capacity is None:
            super().append(value)
        elif self.top == self._capacity - 1:
            raise StackOverFlow("Stack is Full.")
        else:
            super().append(value)
    
    @property
    def peek(self) -> Any:
        if self.top == -1:
            raise StackUnderFlow("Stack is empty.")
        
        return super().__getitem__(self.top)
    
    @property
    def isEmpty(self) -> bool:
        return self.top == -1
    
    @property
    def size(self) -> int:
        return self.top + 1
    
    @property
    def capacity(self) -> Union[float, int]:
        return self._capacity if self._capacity is not None else float('inf')
    
    @property
    def sum(self) -> Union[int, float]:
        """`Returns the sum of all elements in the stack`
        
        Raises StackError if the elements are not int or float.
        """
        sum = 0
        for x in self:
            if not isinstance(x, int) and not isinstance(x, float):
                raise StackError(f"Cannot sum Stack elements. Element type found: {type(x)}")
            else:
                sum += x
        return sum
    
    @property
    def convertTolist(self) -> basicList[Any]:
        """`Returns a simple list of all elements in the stack`"""
        stacklist = []
        for x in self:
            stacklist.append(x)
        return stacklist
    
    def joinWith(self, sep: str) -> str:
        """`Returns the elements of the stack as a string separated by a given separator.`
        
        ### Params
        - `sep`: separator that will be in between the elements of the stack.

        `NOTE`: if the element is not str, it will be forcefully typecasted.
        """
        stacklist = self.convertTolist
        if not isinstance(stacklist[0], str):
            string = str(stacklist[0])
        else:
            string = stacklist[0]
        
        for x in stacklist[1:]:
            if isinstance(x, str):
                string += sep + x
            else:
                string += sep + str(x)
        
        return string
    
    @staticmethod
    def infixToPostfix(expression: str) -> str:
        stack = Stack()
        result = []

        for char in expression:
            if is_operand(char):
                result.append(char)
            elif char == '(':
                stack.push(char)
            elif char == ')':
                while not stack.isEmpty and stack.peek != '(':
                    result.append(stack.pop)
                stack.pop # pop '('
            elif char == ' ':
                continue
            else:
                while (not stack.isEmpty and operator_precedence(stack.peek) > operator_precedence(char)) or (not stack.isEmpty and operator_precedence(stack.peek) == operator_precedence(char) and is_left_associative(stack.peek)):
                    result.append(stack.pop)
                stack.push(char) 
        
        while not stack.isEmpty:
            result.append(stack.pop)
        
        return ''.join(result)
    
    @staticmethod
    def infixToPrefix(expression: str) -> str:
        # Reverse the infix expression and change '(' to ')' and vice versa
        expression = expression[::-1]
        expression = expression.replace('(', '#')
        expression = expression.replace(')', '(')
        expression = expression.replace('#', ')')

        # Convert reversed infix to postfix
        postfix = Stack.infixToPostfix(expression)

        # Reverse postfix to get the prefix expression
        return postfix[::-1]
    
    @staticmethod
    def postfixToInfix(expression: str) -> str:
        stack = Stack()
        for char in expression:
            if is_operand(char):
                stack.push(char)
            elif char == ' ':
                continue
            else:
                operand2 = stack.pop
                operand1 = stack.pop
                stack.push(f'({operand1}{char}{operand2})')
        return stack.joinWith('')
    
    @staticmethod
    def prefixToInfix(expression: str) -> str:
        stack = Stack()
        for char in expression[::-1]:
            if not is_operator(char):
                stack.push(char)
            elif char == ' ':
                continue
            else:
                operand1 = stack.pop
                operand2 = stack.pop
                stack.push(f'({operand1}{char}{operand2})')
        return stack.pop
    
    @staticmethod
    def postfixToPrefix(expression: str) -> str:
        infix = Stack.postfixToInfix(expression)
        return Stack.infixToPrefix(infix)
    
    @staticmethod
    def prefixToPostfix(expression: str) -> str:
        infix = Stack.prefixToInfix(expression)
        return Stack.infixToPostfix(infix)
    
    ROMAN_VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ROMAN_PAIRS = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    
    @staticmethod
    def resolveRomanNumber(number_expression: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        stack = Stack()

        for numeral in number_expression:
            value = roman[numeral]

            if not stack.isEmpty and value > stack.peek:
                last = stack.pop
                stack.push(value - last)
            else:
                stack.push(value)
        
        return stack.sum
    
    @staticmethod
    def generateRomanNumber(number: int) -> str:
        roman_pairs = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]

        stack = Stack()

        for roman, val in roman_pairs:
            while number >= val:
                stack.push(roman)
                number -= val
        
        return stack.joinWith('')

# infix, postfix, prefix
def operator_precedence(op: str) -> int:
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def is_left_associative(op: str) -> bool:
    if op == '^':
        return False  # '^' is right associative
    return True 

def is_operator(c: str) -> bool:
    return c in ['+', '-', '*', '/', '^']

def is_operand(c: str) -> bool:
    return c.isalpha() or c.isdigit()

