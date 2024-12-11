
from typing import List as basicList, Union, Iterable, Any, Callable, overload, Tuple
from .list import List
from ..exceptions import NodeError, LinkedListError

class SingleLinkNode:
    def __init__(
            self,
            value: Union[Any, None] = None,
            next: Union['SingleLinkNode', None] = None,
        ) -> None:

        self._value = value
        self._next = next
    
    @property
    def value(self) -> Any:
        return self._value
    
    @value.setter
    def value(self, value: Union[Any, None]) -> None:
        self._value = value
    
    @value.deleter
    def value(self) -> None:
        self.value = None
    
    @property
    def next(self) -> Union['SingleLinkNode', None]:
        return self._next
    
    @next.setter
    def next(self, next: Union['SingleLinkNode', None]) -> None:
        if not isinstance(next, SingleLinkNode) and next is not None:
            raise NodeError(f"next should be <class 'modestore.python.linkedlist.SingleLinkNode'>. Found -> {type(next)}")
        self._next = next
    
    @next.deleter
    def next(self) -> None:
        self._next = None
    
    @property
    def all_connected_values(self) -> List[Any]:
        values = List([self.value])
        itr = self.next
        while itr is not None:
            values.append(itr.value)
            itr = itr.next
        return values
    
    def __str__(self) -> str:
        return f'[{self.value} --> {self.next}]'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, SingleLinkNode):
            return False
        
        return self.value == value.value and self.next == value.next
    
    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value=value)
    
    def __lt__(self, value: object) -> bool:
        if value is None:
            return False
        
        if not isinstance(value, SingleLinkNode):
            raise NodeError("Cannot compare non Single Node object with Single Node object")
        
        if self.value != value.value:
            return self.value < value.value
        elif self.next is None and value.next is not None:
            return True # shorter self
        elif self.next is not None and value.next is None:
            return False # Longer self
        elif self.next is None and value.next is None:
            return False
        else:
            return self.next < value.next
    
    def __le__(self, value: object) -> bool:
        return self < value or self == value
    
    def __gt__(self, value: object) -> bool:
        return not self.__le__(value)
    
    def __ge__(self, value: object) -> bool:
        return not self.__lt__(value)

class LinkedListOne:
    def __init__(self, __from__: Union[basicList[Any], List[Any], Iterable[Any], SingleLinkNode, 'LinkedListOne'] = []) -> None:
        self._head: SingleLinkNode = SingleLinkNode()

        # create the list if any,
        if __from__:
            if isinstance(__from__, SingleLinkNode):
                itr = __from__
                while itr is not None:
                    self.add_node(itr.value)
                    itr = itr.next
            elif isinstance(__from__, LinkedListOne):
                return self.__init__(__from__.head)
            else:
                for value in __from__:
                    self.add_node(node=SingleLinkNode(value))
    
    def __str__(self) -> str:
        values = self.values
        return ' --> '.join(list(map(str, values))) + ' --> None\n|\nhead' if len(values) > 0 else 'Empty'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    @property
    def head(self) -> Union[SingleLinkNode, None]:
        return self._head.next
    
    @head.setter
    def head(self, head: Union[SingleLinkNode, 'LinkedListOne', None]) -> None:
        if isinstance(head, SingleLinkNode):
            self._head = SingleLinkNode(None, next=head)
        elif isinstance(head, LinkedListOne):
            self._head = SingleLinkNode(None, next=head.head)
        elif head is None:
            self._head = SingleLinkNode()
        else:
            raise LinkedListError("'head' of LinkedListOne must be SingleLinkNode or LinkedListOne itself (later will replace current list with the new one.) or None.")
    
    @head.deleter
    def head(self) -> None:
        self._head = SingleLinkNode()

    def add_node(self, value: Union[Any, None] = None, next: Union[SingleLinkNode, None] = None, node: Union[SingleLinkNode, None] = None) -> None:
        iterator = self._head
        while iterator.next is not None:
            iterator = iterator.next
        
        if value:
            iterator.next = SingleLinkNode(value=value, next=next)
        elif node:
            iterator.next = node
        else:
            pass
    
    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        elif self.head.next is None:
            return 1
        else:
            iterator = self.head
            count = 0
            while iterator is not None:
                count += 1
                iterator = iterator.next
            return count
    
    @property
    def values(self) -> List[Any]:
        vals = List()
        
        iterator = self.head
        while iterator is not None:
            vals.append(iterator.value)
            iterator = iterator.next
        
        return vals

    @property
    def links(self) -> List[SingleLinkNode]:
        links = List()
        iterator = self.head
        while iterator is not None:
            links.append(iterator)
            iterator = iterator.next
        return links
    
    def remove_at(self, **kwargs) -> None:
        # Errors
        if 'pos' in kwargs:
            if not isinstance(kwargs['pos'], int):
                raise LinkedListError(LinkedListError.PARAM_GT_ZERO.format('pos'))
            elif kwargs['pos'] <= 0:
                raise LinkedListError(LinkedListError.PARAM_NOT_ZERO_OR_LESS.format('pos'))
        elif 'position' in kwargs:
            if not isinstance(kwargs['position'], int):
                raise LinkedListError(LinkedListError.PARAM_GT_ZERO.format('position'))
            elif kwargs['position'] <= 0:
                raise LinkedListError(LinkedListError.PARAM_NOT_ZERO_OR_LESS.format('position'))
        elif 'idx' in kwargs and not isinstance(kwargs['idx'], int):
            raise LinkedListError(LinkedListError.PARAM_GT_EQ_ZERO.format('idx'))
        elif 'index' in kwargs and not isinstance(kwargs['index'], int):
            raise LinkedListError(LinkedListError.PARAM_GT_EQ_ZERO.format('index'))

        # Process
        if 'idx' in kwargs:
            index = kwargs['idx'] if kwargs['idx'] >= 0 else self.length + kwargs['idx']
        elif 'index' in kwargs:
            index = kwargs['index'] if kwargs['index'] >= 0 else self.length + kwargs['index']
        elif 'pos' in kwargs:
            index = kwargs['pos'] - 1
        elif 'position' in kwargs:
            index = kwargs['position'] - 1
        else:
            index = self.length - 1
        
        if index >= self.length:
            raise LinkedListError("Cannot Delete at specified index or position: Linked List is too short.")
        
        prev = self._head
        itr = prev.next

        while index != 0:
            index -= 1
            prev = prev.next
            itr = prev.next
        
        if itr.next is None:
            del prev.next
        else:
            prev.next = itr.next
        del itr.next
    
    @property
    def remove_from_end(self) -> None:
        self.remove_at(idx=-1)
    
    @property
    def remove_from_beginning(self) -> None:
        self.remove_at(idx=0)
    
    def remove(self, value: Any) -> None:
        values = self.values
        if value in values:
            index = []
            for i in range(values.length):
                if values[i] == value:
                    index.append(i)
            
            for idx in index:
                self.remove_at(idx=idx)
    
    def insert_at(self, value: Union[Any, None] = None, next: Union[SingleLinkNode, None] = None, node: Union[SingleLinkNode, None] = None, **kwargs) -> None:
        # Errors and processing
        if 'pos' in kwargs:
            if not isinstance(kwargs['pos'], int):
                raise LinkedListError(LinkedListError.PARAM_GT_ZERO.format('pos'))
            elif kwargs['pos'] <= 0:
                raise LinkedListError(LinkedListError.PARAM_NOT_ZERO_OR_LESS.format('pos'))
            
            index = kwargs['pos'] - 1
            
        elif 'position' in kwargs:
            if not isinstance(kwargs['position'], int):
                raise LinkedListError(LinkedListError.PARAM_GT_ZERO.format('position'))
            elif kwargs['pos'] <= 0:
                raise LinkedListError(LinkedListError.PARAM_NOT_ZERO_OR_LESS.format('position'))
            
            index = kwargs['position'] - 1
        elif 'idx' in kwargs:
            if not isinstance(kwargs['idx'], int):
                raise LinkedListError(LinkedListError.PARAM_GT_EQ_ZERO.format('idx'))
            
            index = kwargs['idx'] if kwargs['idx'] >= 0 else self.length + kwargs['idx'] + 1
        elif 'index' in kwargs:
            if not isinstance(kwargs['index'], int):
                raise LinkedListError(LinkedListError.PARAM_GT_EQ_ZERO.format('index'))
            
            index = kwargs['index'] if kwargs['index'] >= 0 else self.length + kwargs['index'] + 1
        else:
            index = self.length - 1
        
        if index > self.length:
            index = self.length
        
        prev = self._head
        itr = prev.next

        while index != 0:
            index -= 1
            prev = prev.next
            itr = prev.next
        
        if node is None and value is not None:
            
            prev.next = SingleLinkNode(value=value, next=next)
            prev = prev.next
            prev.next = next
            while prev.next is not None:
                prev = prev.next
            prev.next = itr
        elif value is None and node is not None:
            
            prev.next = node
            prev = prev.next

            if prev.next is not None:
                while prev.next is not None:
                    prev = prev.next
            
            prev.next = itr
        else:
            raise LinkedListError(LinkedListError.PARAMS_NOT_NONE)
            
    
    def insert_at_beginning(self, value: Union[Any, None] = None, next: Union[SingleLinkNode, None] = None, node: Union[SingleLinkNode, None] = None) -> None:
        if value is not None and node is None:
            self.insert_at(value=value, next=next, idx=0)
        elif value is None and node is not None:
            self.insert_at(node=node, idx=0)
        else:
            raise LinkedListError(LinkedListError.PARAMS_NOT_NONE)
    
    def insert_at_end(self, value: Union[Any, None] = None, next: Union[SingleLinkNode, None] = None, node: Union[SingleLinkNode, None] = None) -> None:
        if value is not None and node is None:
            self.insert_at(value=value, next=next, idx=-1)
        elif value is None and node is not None:
            self.insert_at(node=node, idx=-1)
        else:
            raise LinkedListError(LinkedListError.PARAMS_NOT_NONE)
    
    def search_check(self, token: Union[Any, SingleLinkNode, 'LinkedListOne']) -> bool:
        if isinstance(token, SingleLinkNode):
            itr = self.head
            while itr is not None:
                if itr == token:
                    return True
                itr = itr.next
            return False
        elif isinstance(token, LinkedListOne):
            return self.search_check(token.head)
        else:
            return token in self.values
    
    def search(self, token: Union[Any, SingleLinkNode, 'LinkedListOne']) -> Union[int, None]:
        if self.search_check(token):
            if isinstance(token, SingleLinkNode):
                itr = self.head
                count = 0
                while itr is not None:
                    if itr == token:
                        return count
                    itr = itr.next
                    count += 1
                return None
            elif isinstance(token, LinkedListOne):
                return self.search(token.head)
            else:
                try:
                    return self.values.index(token)
                except ValueError:
                    return None
        else:
            return None
    
    def get_node(self, **kwargs) -> SingleLinkNode:
        # Errors and Processing
        if 'pos' in kwargs:
            if not isinstance(kwargs['pos'], int):
                raise LinkedListError(LinkedListError.PARAM_GT_ZERO.format('pos'))
            elif kwargs['pos'] <= 0:
                raise LinkedListError(LinkedListError.PARAM_NOT_ZERO_OR_LESS.format('pos'))
            
            index = kwargs['pos'] - 1
            
        elif 'position' in kwargs:
            if not isinstance(kwargs['position'], int):
                raise LinkedListError(LinkedListError.PARAM_GT_ZERO.format('position'))
            elif kwargs['pos'] <= 0:
                raise LinkedListError(LinkedListError.PARAM_NOT_ZERO_OR_LESS.format('position'))
            
            index = kwargs['position'] - 1
        elif 'idx' in kwargs:
            if not isinstance(kwargs['idx'], int):
                raise LinkedListError(LinkedListError.PARAM_GT_EQ_ZERO.format('idx'))
            
            index = kwargs['idx'] if kwargs['idx'] >= 0 else self.length + kwargs['idx']
        elif 'index' in kwargs:
            if not isinstance(kwargs['index'], int):
                raise LinkedListError(LinkedListError.PARAM_GT_EQ_ZERO.format('index'))
            
            index = kwargs['index'] if kwargs['index'] >= 0 else self.length + kwargs['index']
        else:
            index = self.length - 1
        
        if index >= self.length:
            raise LinkedListError(f"Cannot get node at the specified location, Does not exist.")
        
        prev = self._head
        itr = prev.next

        while index != 0:
            index -= 1
            prev = prev.next
            itr = prev.next
        
        return itr
    
    @property
    def traverse(self) -> List[Any]:
        return self.values
    
    @property
    def reversed(self) -> 'LinkedListOne':
        values = self.values
        head = LinkedListOne()

        for val in values[::-1]:
            head.add_node(node=SingleLinkNode(val))
        
        return head
    
    @property
    def reverse(self) -> None:
        self._head = self.reversed._head
    
    @property
    def has_cycle(self) -> bool:
        slow = fast = self._head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    
    @property
    def clear(self) -> None:
        self._head = SingleLinkNode()
    
    @property
    def is_empty(self) -> bool:
        return self.head is None
    
    def sort(self, *, key: Union[Callable, None] = None, reverse: bool = False) -> None:
        values = self.values
        values.sort(key=key, reverse=reverse)

        self._head = SingleLinkNode()
        itr = self._head
        for value in values:
            itr.next = SingleLinkNode(value)
            itr = itr.next
    
    @property
    def middle(self) -> SingleLinkNode:
        # returns first middle in case of even number of elements
        if self.length % 2 != 0:
            middle = self.length // 2
        else:
            middle = self.length // 2 - 1
        
        itr = self.head
        while middle != 0:
            itr = itr.next
            middle -= 1
        
        return itr
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, LinkedListOne):
            return False
        
        return self.head.__eq__(value.head)
    
    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
    
    def __lt__(self, value: object) -> bool:
        if value is None:
            return False
        
        if not isinstance(value, LinkedListOne):
            raise LinkedListError("Cannot compare non linked list object with linked list object")
        
        return self.head.__lt__(value.head)
    
    def __le__(self, value: object) -> bool:
        if value is None:
            if self.head is None:
                return True
            else:
                return False
        
        if not isinstance(value, LinkedListOne):
            raise LinkedListError("Cannot compare non linked list object with linked list object")
        
        return self.head.__le__(value.head)
    
    def __gt__(self, value: object) -> bool:
        if value is None:
            if self.head is None:
                return False
            else:
                return True
        
        if not isinstance(value, LinkedListOne):
            raise LinkedListError("Cannot compare non linked list object with linked list object")
        
        return not self.__le__(value)
    
    def __ge__(self, value: object) -> bool:
        if value is None:
            return True
        
        if not isinstance(value, LinkedListOne):
            raise LinkedListError("Cannot compare non linked list object with linked list object")
        
        return not self.__lt__(value)

################### LRU Cache ###########################

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._cache = LinkedListOne([('head', 0), ('tail', 0)])
    
    def _search(self, key: Any, value: Any = None, debug: bool = False) -> Union[Tuple[SingleLinkNode, SingleLinkNode], None]:
        # If debug is true, print the cache and the search details
        if debug:
            print(f"Searching started for key: {key} and value: {value}.\nCache: {self._cache.head}")
        
        # If the cache is empty, return None
        if self._cache.head.next.value == ('tail', 0):
            return None
        
        # Iterate the cache and find if the key exists
        iterator = self._cache
        iterator_2 = iterator.next

        while iterator_2.value != ('tail', 0):
            if value is None and iterator_2.value[0] == key:
                return iterator, iterator_2
            elif value is not None and iterator_2.value == (key, value):
                return iterator, iterator_2
            
            iterator = iterator_2
            iterator_2 = iterator_2.next
        
        return None
    
    @property
    def size(self) -> int:
        return self._cache.length - 2
    
    @size.setter
    def size(self, size: int) -> None:
        raise LinkedListError("Cannot set size of LRU Cache.")
    
    @size.deleter
    def size(self) -> None:
        raise LinkedListError("Cannot delete size of LRU Cache.")
    
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity: int) -> None:
        self._capacity = capacity
    
    @capacity.deleter
    def capacity(self) -> None:
        raise LinkedListError("Cannot delete capacity of LRU Cache.")
    
    def _remove_node(self, prev: SingleLinkNode, target: SingleLinkNode) -> None:
        prev.next = target.next
        del target
    
    def set(self, key: Any, value: Any, debug: bool = False) -> None:
        search_object = self._search(key, value, debug)

        if search_object is not None:
            # update the value, search object is a tuple of (prev, target)
            search_object[1].value = (key, value)
            if debug:
                print(f"Value updated for key: {key}\nCache: {self._cache.head}")
        else:
            # check capacity
            if self.size < self.capacity:
                # add the new key, value pair at the start of the cache after the ('head', 0)
                self._cache.insert_at(node=SingleLinkNode((key, value)), pos=1)
                if debug:
                    print(f"Added new value for key: {key}\nCache: {self._cache.head}")
            else:
                # remove the last node of the cache and add the new key, value pair at the start of the cache after the ('head', 0)
                self._remove_node(self._cache.head, self._cache.tail.prev)
                if debug:
                    print(f"Removed last node of the cache\nCache: {self._cache.head}")
                self._cache.insert_at(node=SingleLinkNode((key, value)), pos=1)
                if debug:
                    print(f"Added new value for key: {key}\nCache: {self._cache.head}")
    
    def get(self, key: Any, debug: bool = False) -> int:
        search_object = self._search(key, debug=debug)

        if search_object is not None:
            # remove the node from its position and add it to the start of the cache
            self._remove_node(search_object[0], search_object[1])
            self._cache.insert_at(node=search_object[1], pos=1)
            return search_object[1].value[1]
        else:
            return -1

################### Doubly Linked List ###########################

class DoubleLinkNode:
    def __init__(
            self,
            value: Union[Any, None] = None,
            prev: Union['DoubleLinkNode', None] = None,
            next: Union['DoubleLinkNode', None] = None
        ) -> None:

        self._value = value
        self._prev = prev
        self._next = next
    
    @property
    def value(self) -> Any:
        return self._value
    
    @value.setter
    def value(self, value: Union[Any, None]) -> None:
        self._value = value
    
    @value.deleter
    def value(self) -> None:
        self.value = None
    
    @property
    def prev(self) -> Union['DoubleLinkNode', None]:
        return self._prev
    
    @prev.setter
    def prev(self, prev: Union['DoubleLinkNode', None]) -> None:
        if not isinstance(prev, DoubleLinkNode) and prev is not None:
            raise NodeError(f"next should be <class 'modestore.python.linkedlist.DoubleLinkNode'>. Found -> {type(next)}")
        self._prev = prev
    
    @prev.deleter
    def prev(self) -> None:
        self._prev = None
    
    @property
    def next(self) -> Union['DoubleLinkNode', None]:
        return self._next
    
    @next.setter
    def next(self, next: Union['DoubleLinkNode', None]) -> None:
        if not isinstance(next, DoubleLinkNode) and next is not None:
            raise NodeError(f"next should be <class 'modestore.python.linkedlist.DoubleLinkNode'>. Found -> {type(next)}")
        self._next = next
    
    @next.deleter
    def next(self) -> None:
        self._next = None
    
    @property
    def all_connected_values(self) -> List[Any]:
        values = List([self.value])
        itr = self.next
        while itr is not None:
            values.append(itr.value)
            itr = itr.next
        return values
    
    def __str__(self) -> str:
        return f'[{self.value} <--> {self.next}]'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, DoubleLinkNode):
            return False

        return self.prev == value.prev and self.value == value.value and self.next == value.next
    
    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
    
    def __lt__(self, value: object) -> bool:
        if value is None:
            return False
        
        if not isinstance(value, DoubleLinkNode):
            raise LinkedListError("Cannot compare non linked list object with linked list object")
        
        if self.value != value.value:
            return self.value < value.value
        elif self.next is None and value.next is not None:
            return True # shorter self
        elif self.next is not None and value.next is None:
            return False # Longer Self
        elif self.next is None and value.next is None:
            return False
        else:
            return self.next < value.next
    
    def __le__(self, value: object) -> bool:
        return self < value or self == value
    
    def __gt__(self, value: object) -> bool:
        return not self.__le__(value)
    
    def __ge__(self, value: object) -> bool:
        return not self.__lt__(value)

class LinkedListTwo:
    def __init__(self, __from__: Union[basicList[Any], List[Any], Iterable[Any], SingleLinkNode, LinkedListOne, DoubleLinkNode, 'LinkedListTwo'] = []) -> None:
        self._head = DoubleLinkNode()

        if __from__:
            if isinstance(__from__, SingleLinkNode):
                itr1 = __from__
                while itr1 is not None:
                    pass
    
    @property
    def head(self) -> Union[DoubleLinkNode, None]:
        h = self._head.next
        if h is None:
            return None
        else:
            h.prev = None
            return h
    
    @head.setter
    def head(self, head: Union[DoubleLinkNode, 'LinkedListTwo', None]) -> None:
        if isinstance(head, DoubleLinkNode):
            self._head = DoubleLinkNode(next=head)
            actual_head = self._head.next
            actual_head.prev = self._head
        elif isinstance(head, LinkedListTwo):
            self._head = head._head
        else:
            raise LinkedListError(f"head should be <class 'modestore.python.linkedlist.DoubleLinkNode'> or <class 'modestore.python.linkedlist.LinkedListTwo'>. Found -> {type(head)}")
        

class MultiLinkNode:
    pass

class LinkedListMulti:
    pass