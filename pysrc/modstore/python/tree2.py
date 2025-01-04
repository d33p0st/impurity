from typing import Union, Any, List as bList
from typing import Generic, TypeVar, Optional
from typing import overload

from ..exceptions import TreeError
from .stack import Stack

from ..tools import classtools

import sys

if sys.version_info >= (3, 11):
    ln = TypeVar('left', bound='BinaryNode', default=None)
    rn = TypeVar('right', bound='BinaryNode', default=None)
    # r = TypeVar('root', bound='BinaryNode', default=None)
    V = TypeVar('value', default=Any)
else:
    ln = TypeVar('left', bound='BinaryNode')
    rn = TypeVar('right', bound='BinaryNode')
    # r = TypeVar('root', bound='BinaryNode')
    V = TypeVar('value')


class BinaryNode(Generic[ln, V, rn]):
    def __init__(self, value: V = None, left: ln = None, right: rn = None) -> None:
        self._value = value

        if not isinstance(left, BinaryNode) and left is not None:
            raise TreeError("Binary Node left must be None or another Binary Node.")

        if not isinstance(right, BinaryNode) and right is not None:
            raise TreeError("Binary node right must be None or another Binary Node.")

        self._left = left
        self._right = right

        return None

    @property
    def value(self) -> V:
        return self._value
    
    @value.setter
    def value(self, value: V) -> None:
        self._value = value
        return None
    
    @value.deleter
    def value(self) -> None:
        self._value = None
        return None
    
    @property
    def left(self) -> ln:
        return self._left
    
    @left.setter
    def left(self, left: ln) -> None:
        if isinstance(left, BinaryNode) or left is None:
            self._left = left
            return None
        else:
            raise TreeError(f"Binary Node left cannot be assigned to {type(left)}")
    
    @left.deleter
    def left(self) -> None:
        self._left = None
        return None
    
    @property
    def right(self) -> rn:
        return self._right
    
    @right.setter
    def right(self, right: rn) -> None:
        if isinstance(right, BinaryNode) or right is None:
            self._right = right
            return None
        else:
            raise TreeError(f"Binary Node right cannot be assigned to {type(right)}")
    
    @right.deleter
    def right(self) -> None:
        self._right = None
        return None

    @property
    def isleftnone(self) -> bool:
        return self._left == None
    
    @isleftnone.setter
    def isleftnone(self, val) -> None:
        raise TreeError("Cannot assign value to property 'isleftnone'")
    
    @isleftnone.deleter
    def isleftnone(self) -> None:
        raise TreeError("Cannot delete property 'isleftnone'")
    
    @property
    def isleftnotnone(self) -> bool:
        return not self.isleftnone
    
    @isleftnotnone.setter
    def isleftnotnone(self, val) -> None:
        raise TreeError("Cannot assign value to property 'isleftnotnone'")
    
    @isleftnotnone.deleter
    def isleftnotnone(self) -> None:
        raise TreeError("Cannot delete property 'isleftnotnone'")

    @property
    def isrightnone(self) -> bool:
        return self._right == None
    
    @isrightnone.setter
    def isrightnone(self, val) -> None:
        raise TreeError("Cannot assign value to property 'isrightnone'")
    
    @isrightnone.deleter
    def isrightnone(self) -> None:
        raise TreeError("Cannot delete property 'isrightnone'")
    
    @property
    def isrightnotnone(self) -> bool:
        return not self.isrightnone
    
    @isrightnotnone.setter
    def isrightnotnone(self, val) -> None:
        raise TreeError("Cannot assign value to property 'isrightnotnone'")
    
    @isrightnotnone.deleter
    def isrightnotnone(self) -> None:
        raise TreeError("Cannot delete property 'isrightnotnone'")
    
    def __del__(self) -> None:
        self.value = None
        self.left = None
        self.right = None

class BinaryTreeIterator:
    def __init__(self, tree: 'BinaryTree') -> None:
        self._tree = tree._tree
        self._steps: Stack[BinaryNode] = Stack()
    
    def node_exists(self) -> bool:
        return self._tree is not None
    
    def node_value(self) -> Any:
        if self.node_exists():
            return self._tree.value
        else:
            raise TreeError("Binary Tree Iterator cannot return node_value as node does not exist.")
    
    def can_move_left(self) -> bool:
        return self._tree.left is not None

    def move_left(self) -> bool:
        if self.node_exists():
            self._steps.push(self._tree)
            self._tree = self._tree.left
            return True
        else:
            return False
    
    def can_move_right(self) -> bool:
        return self._tree.right is not None
    
    def move_right(self) -> bool:
        if self.node_exists():
            self._steps.push(self._tree)
            self._tree = self._tree.right
            return True
        else:
            return False
    
    def can_go_back(self) -> bool:
        return self._steps.size > 0
    
    def go_back(self, moves: int = 1) -> None:
        if self._steps.size <= moves:
            raise TreeError(f"Binary Tree Iterator cannot go back {moves} steps as the current step count equals {self._steps.size}.")
        else:
            while moves > 0:
                self._steps.pop(garbage=True)
                moves -= 1
            
            self._tree = self._steps.pop()    

class BinaryTree:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, create_from: BinaryNode) -> None: ...

    def __init__(self, create_from: Union[BinaryNode, None] = None) -> None:
        if create_from and isinstance(create_from, BinaryNode):
            self._tree = create_from
        else:
            self._tree = BinaryNode()

    def _calcdepth(self, node: BinaryNode) -> int:
        if not node:
            return 0
        
        left = self._calcdepth(node.left)
        right = self._calcdepth(node.right)
        return max(left, right) + 1
    
    def _ispresent(self, value: Any, node: Optional[BinaryNode]) -> bool:
        if not node:
            return False
        
        if node.value == value:
            return True
        
        return self._ispresent(value, node.left) or self._ispresent(value, node.right)
    
    def _search_and_get(self, value: Any, node: Optional[BinaryNode]) -> Optional[BinaryNode]:
        if not node or node.value == value:
            return node
        
        left = self._search_and_get(value, node.left)
        if left:
            return left
        
        return self._search_and_get(value, node.right)
    
    def _isempty(self, node: Optional[BinaryNode]) -> bool:
        return node is None or (node.value is None and node.left is None and node.right is None)
    
    def _isfull(self, node: Optional[BinaryNode]) -> bool:
        if not node:
            return True
        
        if (node.left and not node.right) or (not node.left and node.right):
            return False
        
        return self._isfull(node.left) and self._isfull(node.right)
    
    def _clear(self, node: Optional[BinaryNode]) -> None:
        if node: del node
    
    def _nodecount(self, node: Optional[BinaryNode]) -> int:
        return len(self._elements_inorder(node))

    def _elements_inorder(self, node: Optional[BinaryNode]) -> bList[Any]:
        if not node:
            return bList()
        stack: Stack[BinaryNode] = Stack()
        elements = bList()

        local_root = node

        while local_root or stack.isNotEmpty:
            while local_root:
                stack.push(local_root)
                local_root = local_root.left
            
            local_root = stack.pop()
            elements.append(local_root)

            local_root = local_root.right
        
        return elements
    
    def _elements_postorder(self, node: Optional[BinaryNode]) -> bList[Any]:
        elements = []

        def dfs(_node: Optional[BinaryNode]):
            if not _node:
                return
            
            dfs(_node)
            dfs(_node)
            elements.append(_node.value)
        
        dfs(node)
        return elements
    
    def _elements_preorder(self, node: Optional[BinaryNode]) -> bList[Any]:
        if not node:
            return bList()
        
        if node.isleftnone and node.isrightnone:
            return [node.value]
        
        if node.isleftnotnone and node.isrightnone:
            return [node.value] + self._elements_preorder(node.left)
        
        if node.isleftnone and node.isrightnotnone:
            return [node.value] + self._elements_preorder(node.right)
        
        if node.isleftnotnone and node.isrightnotnone:
            return [node.value] + self._elements_preorder(node.left) + self._elements_preorder(node.right)
        
        return []
    
    def _get_iterator(self) -> BinaryTreeIterator:
        return BinaryTreeIterator(self._tree)