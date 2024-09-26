## Stack Docs

A `stack` is a linear data structure that follows the Last In First Out (LIFO) principle, where the most recently added element is the first to be removed. Operations typically include:

- Push
- Pop
- Peek
- isEmpty

### Features

- **Disabled `[]`**: The usage of `[]` for setting, getting or deleting an element is disabled and will generate `StackError`.

- **Vast Range of Utilities**: Several utilities are available directly inbuilt inside the class that can be used for either testing purpose or projects or the unavoidable cheating in exams (not made for this purpose.).

- **Can be Generated from [List](/docs/List/list.md) Class**: The [List](/docs/List/list.md) class available under `modstore.python` can convert itself to `Stack` or can be explicitly passed to `Stack`'s `__init__` method (meaning, if you have a [List](/docs/List/list.md) type variable you can create a stack by `Stack(variable)`). We will look into it Later.

- **All `Stack` behaviour**: The `stack` class is made into a proper implementation of stack and replicates complete stack behaviour `(LIFO)`.

### Usage

Let us now jump to usage.

- [Installation](#installation-if-you-havent-yet)
- [Import](#import-the-stack-class-from-the-python-module-of-modstore-package)
- [Creation](#create-a-stack)
- [Push](#push-into-the-stack)
- [Pop](#pop-from-the-stack)
- [Peek](#peek)
- [Top](#getting-the-top-index)
- [isEmpty](#checking-if-stack-is-empty-or-not)
- [Size](#get-the-size-of-the-stack-filled)
- [Capacity](#get-capacity-of-the-stack)
- [Sum](#get-the-sum-of-all-elements-in-the-stack-only-if-the-elements-are-int-and-float)
- [`''.join() replacement`](#the-join-functionality)
- [STATIC METHODS](#static-methods)

##### Installation (if you haven't yet)

```bash
pip install modstore
```

##### Import the `Stack` class from the python module of `modstore` package

```python
from modstore.python import Stack
```

##### Create a stack

> Empty Stack

```python
stack = Stack(capacity=10) # sets capacity of the stack to 10.
# set it to None for infinity or no limit.
```

> From python's inbuilt list

```python
stack = Stack([1, 2, 3, 4, 5])
```

> From `modstore.python`'s List

```python
from modstore.python import List

somelist = List([1, 2, 3, 4, 5])

# now there's three ways to do this
# option 1
somestack = somelist.convertToStack # this will create a stack with infinite capacity

# option 2
somestack = somelist.convertToStackWithCapacity(capacity=10)
# this sets the capacity too
# if the given capacity is less than the number of elements
# in the list, it will raise ValueError

# option 3

somestack = Stack(somelist) 
# this is what I was talking about in the Features Section.
```

##### Push into the stack

```python
stack.push(1)
stack.push("abc")
```

##### Pop from the stack

```python
top_value = stack.pop
```

##### Peek

`Peek` means getting the value at the top of the stack without popping it.

```python
value_at_top = stack.peek
```

##### Getting the top index

```python
top = stack.top
```

##### Checking if stack is Empty or not

```python
if stack.isEmpty:
    print("Stack is empty")
else:
    print("Stack is not empty")
```

##### get the size of the stack (filled)

```python
length = stack.size
```

##### Get capacity of the stack

```python
print(stack.capacity) # will print `inf` if infinity else some `int`
```

##### Get the sum of all elements in the stack (only if the elements are `int` and `float`)

```python
stack = Stack()
stack.push(19)
stack.push(20)

print(stack.sum) # will print 39
```

##### The `''.join()` functionality.

```python
print(stack.joinWith('')) # will work the same as ''.join(Some Iterable)
# BONUS: if the elements are not str, it will be forcefully
# typecasted to str.
```

##### STATIC METHODS

These methods don't need to an instance of `Stack` class.

```python
# suppose you want to call some static method named poopoo
# in the stack class.

from modstore.python import Stack

Stack.poopoo(*args, **kwargs) # and it will run

# *args and **kwargs means parameters
```

- Infix, Postfix, Prefix conversion

  ```python
  Stack.infixToPostfix("A+B*(C-D)")
  # will output -> "ABCD-*+"

  Stack.infixToPrefix("A+B*(C-D)")
  # will output -> "+A*B-CD"

  Stack.postfixToInfix("ABCD-*+") # "(A+(B*(C-D)))"

  Stack.postfixToPrefix("ABCD-*+") # "+A*B-CD"

  Stack.prefixToInfix("+A*B-CD") # "(A+(B*(C-D)))"

  Stack.prefixToPostfix("+A*B-CD") # "ABCD-*+"
  ```

  > And Yes, they support white spaces. -_-

- Roman Number and Number Conversion

  ```python
  Stack.resolveRomanNumber("MXCVII") # 1097

  Stack.generateRomanNumber(1097) # MXCVII
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