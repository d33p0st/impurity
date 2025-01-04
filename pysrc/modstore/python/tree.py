
from typing import Any, Union, List as basicList
from typing import Generic, TypeVar
from typing import overload

from ..exceptions import TreeError
from .stack import Stack

import sys

if sys.version_info >= (3, 11):
    left_node = TypeVar('left_node', default=None, bound='BinaryNode')
else:
    left_node = TypeVar('left_node', bound='BinaryNode')

if sys.version_info >= (3, 11):
    Right = TypeVar('Right', bound='BinaryNode', default=None)
else:
    Right = TypeVar('Right', bound='BinaryNode')

if sys.version_info >= (3, 11): 
    Value = TypeVar('Value', default=Any)
else:
    Value = TypeVar('Value')

class BinaryNode(Generic[left_node, Value, Right]):
    def __init__(self, value: Value, left_node_node: left_node = None, right: Right = None) -> None:
        self._value = value

        if isinstance(left_node_node, BinaryNode) or left_node_node is None:
            self._left_node_node = left_node_node
        else:
            raise TreeError("Binary Node left_node_node value must be either another Binary Node or None")
        
        if isinstance(right, BinaryNode) or right is None:
            self._right = right
        else:
            raise TreeError("Binary Node Right value must be either another Binary Node or None")
    
    @property
    def value(self) -> Value:
        return self._value
    
    @value.setter
    def value(self, value: Value) -> None:
        self._value = value
    
    @value.deleter
    def value(self) -> None:
        self._value = None
    
    @property
    def left_node(self) -> left_node:
        return self._left_node_node
    
    @left_node.setter
    def left_node_node(self, left_node_node: left_node) -> None:
        if isinstance(left_node_node, BinaryNode) or left_node_node is None:
            self._left_node = left_node
        else:
            raise TreeError("Binary Node left_node value must be either another Binary Node or None")
    
    @left_node.deleter
    def left_node(self) -> None:
        self._left_node = None
    
    @property
    def right(self) -> Right:
        return self._right
    
    @right.setter
    def right(self, right: Right) -> None:
        if isinstance(right, BinaryNode) or right is None:
            self._right = right
        else:
            raise TreeError("Binary Node Right value must be either another Binary Node or None")
    
    @right.deleter
    def right(self) -> None:
        self._right = None
    
    def __del__(self) -> None:
        self.value = None
        self.left_node = None
        self.right = None

# class BinaryTree(Generic[Root]):
#     def __init__(self, root: BinaryNode[left_node, Value, Right]) -> None:
#         if not isinstance(root, BinaryNode) or root is None:
#             raise TreeError("'root' parameter of BinaryTree Must be a <class 'BinaryNode'>")
#         self._root = root
    
#     # @property
#     # def root(self):
#     #     return self._root

#     # @root.setter
#     # def root(self, root: ) -> None:
#     #     if not isinstance(root, BinaryNode) and root is not None:
#     #         raise TreeError("'root' parameter of BinaryTree Must be a <class 'BinaryNode'> or None")
#     #     self._root = root
    
#     # @root.deleter
#     # def root(self) -> None:
#     #     self._root = None
    
#     def _depth(self, node) -> int:
#         if not node:
#             return 0
        
#         left_node = self._depth(node.left_node)
#         right = self._depth(node.right)
        
#         return max(left_node, right) + 1

#     @property
#     def depth(self) -> int:
#         return self._depth(self._root)
    
#     @depth.setter
#     def depth(self, val: any) -> None:
#         raise TreeError("'depth' cannot be set explicitly.")
    
#     @depth.deleter
#     def depth(self) -> None:
#         raise TreeError("'depth' cannot be deleted.")
    
#     def _search(self, value, node) -> bool:
#         if not node:
#             return False
        
#         if node.value == value:
#             return True
        
#         return self._search(value, node.left_node) or self._search(value, node.right)

#     def search(self, value: Value) -> bool:
#         return self._search(value, self._root)
    
#     def _search_and_get(self, value: Value, node: Union[BinaryNode, None]) -> Union[BinaryNode, None]:
#         if not node:
#             return None
        
#         if node.value == value:
#             return node
        
#         left_node = self._search_and_get(value, node.left_node)
        
#         if left_node is not None:
#             return left_node
        
#         return self._search_and_get(value, node.right)

#     def search_and_get(self, value: Value) -> Union[BinaryNode, None]:
#         return self._search_and_get(value, self._root)
    
#     def isempty(self) -> bool:
#         return self._root is None or (self._root.value is None and self._root.left_node is None and self._root.right is None)
    
#     def _is_full(self, node: Union[BinaryNode, None]) -> bool:
#         if not node:
#             return True
        
#         if (node.left_node and not node.right) or (not node.left_node and node.right):
#             return False
        
#         return self._is_full(node.left_node) and self._is_full(node.right)
    
#     def isfull(self) -> bool:
#         return self._is_full(self._root)
    
#     def clear(self) -> None:
#         if isinstance(self._root, BinaryNode):
#             self._root.__del__()
#         else:
#             self.root = None
    
#     def _nodecount(self, node: Union[BinaryNode, None]) -> int:
#         ...
#         # WRITE IT

#     def nodecount(self) -> int:
#         return self._nodecount(self._root)

#     def get_elements_inorder(self) -> basicList[Any]:
#         stack: Stack[BinaryNode] = Stack()
#         result = basicList()

#         local_root = self._root
        
#         while local_root or stack.isNotEmpty:
#             while local_root:
#                 stack.push(local_root)
#                 local_root = local_root.left_node
            
#             local_root = stack.pop()
#             result.append(local_root.value)

#             local_root = local_root.right
        
#         return result

# a = BinaryTree(BinaryNode(1))
# a._root

a = BinaryNode(1)
