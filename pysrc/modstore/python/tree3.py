from typing import Generic, TypeVar, Union, Type, Optional
from typing import Any, List as basicList
from typing import overload

from ..exceptions import TreeError
from .stack import Stack
from ..tools import CustomBoolean, Property

left = TypeVar('left', 'BinaryNode', None)
right = TypeVar('right', 'BinaryNode', None)
content = TypeVar('content')

class Possibility(CustomBoolean, Generic[content]):
    def __init__(self, parent: Any, attribute: str, value: content) -> None:
        self._value = value
        self._parent = parent
        self._attribute = attribute
    
    isNone = Property(
        getter=lambda cls: cls._value is None,
        error=TreeError,
        _setter_error_arguments=("Cannot set 'isNone' property.",),
        _deleter_error_arguments=("Cannot delete 'isNone' property.",),
    )

    isNotNone = Property(
        getter=lambda cls: not cls.isNone,
        error = TreeError,
        _setter_error_arguments=(f"Cannot set 'isNotNone' property of ",),
        _deleter_error_arguments=("Cannot delete 'isNotNone' property.",),
    )

    def __bool__(self) -> bool:
        return self.isNotNone
    
    def __call__(self):
        return self._value
    
    def __set__(self, instance: Any, value: Any) -> None:
        if instance is None:
            raise AttributeError(f"Cannot access without initializing.")
        self._value = value
        return setattr(self._parent, self._attribute, value)
    
    def __delete__(self, instance: Any) -> None:
        if instance is None:
            raise AttributeError(f"Cannot access without initializing.")
        self._value = None
        return delattr(self._parent, self._attribute)

class BinaryNode(Generic[left, content, right]):
    def __init__(
            self,
            value: content = None,
            left: left = None,
            right: right = None,
    ) -> None:
        if not isinstance(left, BinaryNode) and left is not None:
            raise TreeError("Binary Node left must be None or another Binary Node.")
        if not isinstance(right, BinaryNode) and right is not None:
            raise TreeError("Binary node right must be None or another Binary Node.")
        self._content = value
        self._left = left
        self._right = right
        return None
    
    validate_left = lambda cls, x: isinstance(x, BinaryNode) or x is None or (_ for _ in ()).throw(
        TreeError("Binary Node left must be None or another Binary Node.")
    )
    validate_right = lambda cls, x: isinstance(x, BinaryNode) or x is None or (_ for _ in ()).throw(
        TreeError("Binary node right must be None or another Binary Node.")
    )

    
    left = Property(
        getter=lambda cls: Possibility(cls, 'left', cls._left),
        setter=lambda cls, value: (cls.validate_left(value), setattr(cls, '_left', value), None)[-1],
        deleter=lambda cls: (setattr(cls, '_left', None), None)[-1],
    )
    
    right = Property(
        getter=lambda cls: Possibility(cls, 'right', cls._right),
        setter=lambda cls, value: (cls.validate_right(value), setattr(cls, '_right', value), None)[-1],
        deleter=lambda cls: (setattr(cls, '_right', None), None)[-1],
    )
    
    value = Property(
        attribute='_content',
        setter=True,
        deleter=True,
    )

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

    def _elements_inorder(self, node: Optional[BinaryNode]) -> basicList[Any]:
        if not node:
            return basicList()
        stack: Stack[BinaryNode] = Stack()
        elements = basicList()

        local_root = node

        while local_root or stack.isNotEmpty:
            while local_root:
                stack.push(local_root)
                local_root = local_root.left
            
            local_root = stack.pop()
            elements.append(local_root)

            local_root = local_root.right
        
        return elements
    
    def _elements_postorder(self, node: Optional[BinaryNode]) -> basicList[Any]:
        elements = []

        def dfs(_node: Optional[BinaryNode]):
            if not _node:
                return
            
            dfs(_node)
            dfs(_node)
            elements.append(_node.value)
        
        dfs(node)
        return elements
    
    def _elements_preorder(self, node: Optional[BinaryNode]) -> basicList[Any]:
        if not node:
            return basicList()
        
        if node.isleftnone and node.isrightnone:
            return [node.value]
        
        if node.isleftnotnone and node.isrightnone:
            return [node.value] + self._elements_preorder(node.left)
        
        if node.isleftnone and node.isrightnotnone:
            return [node.value] + self._elements_preorder(node.right)
        
        if node.isleftnotnone and node.isrightnotnone:
            return [node.value] + self._elements_preorder(node.left) + self._elements_preorder(node.right)
        
        return []
    
    # def _get_iterator(self) -> BinaryTreeIterator:
    #     return BinaryTreeIterator(self._tree)