from typing import List as basicList, Union, Iterable, Any, Callable
from .list import List
from ..exceptions import NodeError, LinkedListError

class SingleLinkNode:
    """`Single Link Node for Singly Linked List`
    
    This class is the bare Singly Linked List class with limited functionality (made for maintaing Linked List Structure.)

    To create a Singly Linked List, use `LinkedListOne`.
    """
    def __init__(
            self,
            value: Union[Any, None] = None,
            next: Union['SingleLinkNode', None] = None,
        ) -> None:
        """`Create a Single Link Node for Singly Linked List.`
        
        This class can be used to create raw singly linked list.

        #### Paramaters

        - `value` -> `[Any, None]` : The value for the node to store.
        - `next` -> `[SingleLinkNode, None]`: The next node of the same type.
        """
        ...
    
    @property
    def value(self) -> Any:
        """`Get the value stored in the Node.`"""
        ...
    
    @value.setter
    def value(self, value: Union[Any, None]) -> None:
        ...
    
    @value.deleter
    def value(self) -> None:
        ...
    
    @property
    def next(self) -> Union['SingleLinkNode', None]:
        """`Get the next Node or None.`"""
        ...
    
    @next.setter
    def next(self, next: 'SingleLinkNode') -> None:
        ...
    
    @next.deleter
    def next(self) -> None:
        ...
    
    @property
    def all_connected_values(self) -> List[Any]:
        """`Get all the values including this node that are connected till the end in the form of a <class 'modstore.python.list.List'>`"""
        ...
    
    def __str__(self) -> str:
        """`String Representation of the node.`"""
        ...
    
    def __repr__(self) -> str:
        """`Repr(node)`"""
        ...
    
    def __eq__(self, value: object) -> bool:
        """`Equality Definition`
        
        equal if the current value and all the connected values are same.
        """
        ...
    
    def __ne__(self, value: object) -> bool:
        """`Opposite of Equality`"""
        ...
    
    def __lt__(self, value: object) -> bool:
        """`Less Than Definition`
        
        Less if shorter or the values are shorter (recursive)
        """
        ...
    
    def __le__(self, value: object) -> bool:
        """`Less than or equal to`"""
        ...
    
    def __gt__(self, value: object) -> bool:
        """`Negative Less than or equal to`"""
        ...
    
    def __ge__(self, value: object) -> bool:
        """`Negative Less Than`"""
        ...
    
class LinkedListOne:
    """`Singly Linked List Wrapper Class`
    
    This is the ideal class to use to create a Singly Linked List.

    To get the raw linked list (in the form of `SingleLinkNode`), use the following technique:

    ```python
    >>> from modstore import LinkedListOne

    >>> some_linked_list = LinkedListOne([1, 2, 3, 4, 5])
    # initiate the list with the given values
    
    # the above some_linked_list is
    # of the type LinkedListOne
    >>> raw_linked_list = some_linked_list.head
    ```

    `This class contains a alot of pre-built method for Singly Linked List operations.`
    """
    def __init__(
            self,
            __from__: Union[basicList[Any], List[Any], Iterable[Any], SingleLinkNode, 'LinkedListOne'] = []
        ) -> None:
        """`Create a Singly Linked List`
        
        Can be created from builtin `list`, `<class 'modstore.python.list.List'>`, any Iterable (like tuple or dict keys or values or any related inherited class), `SingleLinkNode` or from another `LinkedListOne` object.
        """
        ...
    
    def __str__(self) -> str:
        """`String Representation of the Linked List.`"""
        ...
    
    def __repr__(self) -> str:
        """`repr(linkedlist)`"""
        ...
    
    @property
    def head(self) -> Union[SingleLinkNode, 'LinkedListOne', None]:
        """Return the linked list's head in the form of `SingleLinkNode` if there, else None"""
        ...
    
    @head.setter
    def head(self, head: Union[SingleLinkNode, None]) -> None: ...
    @head.deleter
    def head(self) -> None: ...

    def add_node(
            self,
            value: Union[Any, None] = None,
            next: Union[SingleLinkNode, None] = None,
            node: Union[SingleLinkNode, None] = None,
        ) -> None:
        """`Add a node at the end of the current list.`
        
        This method is different than the `insert_at` or `insert_at_end` method
        and simply adds a node at the end.

        #### parameter description

        You can either provide `value` and `next`, where internally, a `SingleLinkNode` will be created for you
        with the given `value` and `next`. If `next` is not given, it will be set to None.

        Or, you can provide a `node` directly, which needs to be of the type `SingleLinkNode`. This node can any number of have links
        (nodes pointing to other nodes and so on) or could even be the head of some other `LinkedListOne` type object.

        #### Import

        ```python
        >>> from modstore.python.linkedlist import LinkedListOne, SingleLinkNode
        # or
        >>> from modstore.python import LinkedListOne, SingleLinkNode
        # or
        >>> from modstore import LinkedListOne, SingleLinkNode
        ```

        Any of the above works.

        #### Use cases

        ##### 1.
        ```python
        >>> linked_list = LinkedListOne()
        # create an empty linked list.

        >>> linked_list.add_node(value=10)
        # will result in: 10 -> None
        ```

        ##### 2.
        ```python
        >>> linked_list = LinkedListOne()
        >>> linked_list.add_node(value=10, next=SingleLinkNode(11))
        # will result in: 10 -> 11 -> None
        ```

        ##### 3.
        ```python
        >>> some_node_chain = SingleLinkNode(value=10, next=SingleNode(value=10, next=SingleLinkNode(value=30)))
        # this is: 10 -> 20 -> 30 -> None (SingleLinkNode type)

        >>> linked_list = LinkedListOne()
        >>> linked_list.add_node(node=some_node_chain)
        # this will result in: 10 -> 20 -> 30 -> None (LinkedListOne type)
        ```
        """
        ...
    
    @property
    def length(self) -> int:
        """`Length of the current list.`"""
        ...
    
    @property
    def values(self) -> List[Any]:
        """Get a List of all the values of the linked list
        
        This `List` is `<class 'modstore.python.list.List'>`
        """
        ...
    
    @property
    def links(self) -> List[SingleLinkNode]:
        """Get a List of all Links of the linked list.
        
        The `List` is `<class 'modstore.python.list.List'>`

        If Linked List is 1 -> 2 -> 3 -> 4 -> None
        
        This will return:  
        `[1 -> 2 -> 3 -> 4 -> None, 2 -> 3 -> 4 -> None, 3 -> 4 -> None, 4 -> None]`
        """
        ...
    
    def remove_at(
            self,
            *,
            idx: Union[int, None] = None,
            index: Union[int, None] = None,
            pos: Union[int, None] = None,
            position: Union[int, None] = None
        ) -> None:
        """`Remove at a given index or position.`
        
        #### parameter description

        you need to provide either **index** or **position**.  
        To provide **index**, any of the `idx` or `index` can be used.  
        To provide **position** any of the `pos` or `position` can be used.

        `index` or `idx` should be >=0 and < lenght of the list.  
        `pos` or `position` should >= 1 and <= length of the list.

        If none of `idx`, `index` or `pos`, `position` is provided, the last element will be deleted.

        **`NOTE:`** it supports negative indexing, where -1 means the last element and so on.
        """
        ...
    
    @property
    def remove_from_end(self) -> None:
        """`Remove the First Element from the Linked List`"""
        ...
    
    @property
    def remove_from_beginning(self) -> None:
        """`Remove the Last Element from the Linked List`"""
        ...
    
    def remove(self, value: Any) -> None:
        """`Remove all the nodes from the Linked List where the value is equal to specified value.`"""
        ...
    
    def insert_at(
            self,
            value: Union[Any, None] = None,
            next: Union[SingleLinkNode, None] = None,
            node: Union[SingleLinkNode, None] = None,
            *,
            idx: Union[int, None] = None,
            index: Union[int, None] = None,
            pos: Union[int, None] = None,
            position: Union[int, None] = None
        ) -> None:
        """`Insert at a given index or position`
        
        For `index`, use either `idx` or `index` to specify. Can be >=0. If >= length, it will be inserted at the last of the list.

        For `position`, use either `pos` or `position` to specify. Can be >= 1. If > length, it will be inserted at the last of the list.

        `idx`, `index`, `pos`, `position`, out of these four, only one should be used. and that too as keyword argument. Do not Pass as positional argument.

        If none of these four is provided, it will be inserted at the last.

        #### Rest of the parameters (can be positional or keyword as per choice)

        - `value`: Value to be added.
        - `next`: the next link for the value
        - `node`: Node to be added.

        **`NOTE:`** either use `value` and `next` or `node`. where `node` is used, `value` and `next` is not needed.

        If `value`, `next` and `node` all three are provided, `node` will be ignored and only `value` and `next` will be used for insertion.
        """
        ...
    
    def insert_at_beginning(self, value: Union[Any, None] = None, next: Union[SingleLinkNode, None] = None, node: Union[SingleLinkNode, None] = None) -> None:
        """`Insert at the beginning of the List`
        
        Use either `value` and `next` to define a node that is to be inserted,  
        or use only `node` to define a node that is to be inserted.
        """
        ...
    
    def insert_at_end(self, value: Union[Any, None] = None, next: Union[SingleLinkNode, None] = None, node: Union[SingleLinkNode, None] = None) -> None:
        """`Insert at the end of the List.`
        
        Use either `value` and `next` to define a node that is to be inserted,  
        or use only `node` to define a node that is to be inserted.
        """
        ...
    
    def search_check(
            self,
            token: Union[Any, SingleLinkNode, 'LinkedListOne']
        ) -> bool:
        """`Returns True if token exists in the List else False.`
        
        `token` can be a `SingleLinkNode` or `LinkedListOne` or Any other type.

        If `SingleLinkNode` is provided, it will check if the Node exists in the List or not.  
        If `LinkedListOne` is provided, it will check if the `head` exists as a node in the List or not.  
        If Any other type is provided, it will check if that `token` is present among the values of the list or not.
        """
        ...
    
    def search(
            self,
            token: Union[Any, SingleLinkNode, 'LinkedListOne']
        ) -> Union[int, None]:
        """`Returns the index of the Node where the token exists, else None`
        
        `token` can be a `SingleLinkNode` or `LinkedListOne` or Any other type.

        If `SingleLinkNode` is provided, it will check if the Node exists in the List or not. If exists, it will return the index else None.  
        If `LinkedListOne` is provided, it will check if the `head` exists as a node in the List or not. If exists, it will return the index else None.  
        If Any other type is provided, it will check if that `token` is present among the values of the list or not. If exists, it will return the index else None.
        """
        ...
    
    def get_node(self, *, idx: Union[int, None] = None, index: Union[int, None] = None, pos: Union[int, None] = None, position: Union[int, None] = None) -> SingleLinkNode:
        """`Returns a node based on index or position`
        
        Raises `LinkedListError` if `index` or `position` does not exist.

        Any of the four parameters can be given, and only one is needed.

        needless to say, index must be >= 0 and < length, and position must be >= 1 and <= length.
        """
        ...
    
    @property
    def traverse(self) -> List[Any]:
        """`alias for .values property.`"""
        ...
    
    @property
    def reversed(self) -> 'LinkedListOne':
        """`Returns a linked list which is the reverse of the current one.`"""
        ...
    
    @property
    def reverse(self) -> None:
        """`Reverse the current list in place.`"""
        ...
    
    @property
    def has_cycle(self) -> bool:
        """`Checks if the current list has any cycles or not.`"""
        ...
    
    @property
    def clear(self) -> None:
        """`Clear the current List.`"""
        ...
    
    @property
    def is_empty(self) -> bool:
        """`Checks if the current list is empty.`"""
        ...
    
    def sort(self, *, key: Union[Callable, None] = None, reverse: bool = False) -> None:
        """`Sort the linked list in place.`"""
        ...
    
    @property
    def middle(self) -> SingleLinkNode:
        """`Get the middle node.`"""
        ...
    
    def __eq__(self, value: object) -> bool: ...
    def __ne__(self, value: object) -> bool: ...
    def __lt__(self, value: object) -> bool: ...
    def __le__(self, value: object) -> bool: ...
    def __gt__(self, value: object) -> bool: ...
    def __ge__(self, value: object) -> bool: ...

class LRUCache:
    """`Least Recently Used Cache` is a part of cache replacement algorithm.
    
    This implementation uses a Singly Linked List to maintain the cache.
    """
    def __init__(self, capacity: int) -> None:
        """`Create a Least Recently Used Cache`
        
        `capacity` is the maximum number of key-value pairs that can be stored in the cache.
        """
        ...
    
    @property
    def size(self) -> int:
        """`Get the current size of the cache.`"""
        ...
    
    @size.setter
    def size(self, size: int) -> None: ...
    
    @size.deleter
    def size(self) -> None: ...
    
    @property
    def capacity(self) -> int:
        """`Get the maximum number of key-value pairs that can be stored in the cache.`"""
    
    @capacity.setter
    def capacity(self, capacity: int) -> None: ...
    
    @capacity.deleter
    def capacity(self) -> None: ...

    def set(self, key: Any, value: Any, debug: bool = False) -> None:
        """`Set a key-value pair in the cache.`
        
        This searches for the key in the cache. If found, it updates the value.
        If not found, it adds the key-value pair to the cache.

        If the cache is full, it removes the least recently used key-value pair.

        `debug` is a boolean flag to print debug statements.
        """
        ...
    
    def get(self, key: Any, debug: bool = False) -> int:
        """`Get the value of the key.`
        
        This searches for the key in the cache. If found, it returns the value.
        If not found, it returns -1.

        If the key is found, it is moved to the front of the cache. (Least Recently Used)

        `debug` is a boolean flag to print debug statements.
        """
        ...

class DoubleLinkNode:
    ...

class LinkedListTwo:
    ...

class MultiLinkNode:
    ...

class LinkedListMulti:
    ...