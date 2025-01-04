from typing import Optional, Literal, Union, List as basicList, Any
from typing import Callable, TypeVar, Type, Tuple
from typing import overload
from abc import ABC, abstractmethod
from ..exceptions import MethodOverrideError
import inspect

CLASS = TypeVar('CLASS')
METHOD = TypeVar('METHOD')
Element = TypeVar('Element')

class classtools:
    """`classtools` brings the `@override` decorator feature
    (introduced in python3.12), for all python versions.

    With a bit of tinkering with all existing python mechanisms,
    `classtools` provides a simplistic (all complex operations
    kept hidden) way to keep your code error free.

    #### Working:

    `classtools` provides two static-methods to work with,
    `class_override` and `method_override`.

    `method_override` sets the `__override__` attribute of any
    method it is decorated on top of, as True.

    `class_override` is a decorator for `class` objects and
    should be used only on classes that are inheriting some
    other base class. On classes, that do not inherit any other
    base class it will do nothing.

    While using `class_override`, if the child class has properties
    that are overloaded, and either `fset` or `fdel` or both are not
    defined in the child class, `class_override` will make the child
    class use the base class's `fdel` and `fset`.

    Additionally, if any method found in the child class has an
    `__override__` attribute set to True (as a result of
    `method_override` decorator), It will check if the base class has
    that method or not, if not, it will raise `MethodOverrideError`
    (ultimately contributing towards maintaing large code bases (as
    it was for `typing.override`)).

    It will also check, any method having `method_override` decorator
    belongs to a class that is a child class of some other parent class
    or not. If found it is not, `MethodOverrideError` will be raised.

    The methods or properties that are not explicitly defined in the child
    class, will be taken from the base class (no contribution here).

    #### Usage:

    NOTE: This is to be used only in the `.py` file and not in the stubs
    (`.pyi` file). Any method that is overriden does not need to be added
    in the stubs of the child class unless you want a different description
    docstring for that overriden method, it will fetch from the base class
    by default. Remember that this is a runtime check and static type
    checkers wont trigger any errors.

    ```python
    from modstore.tools import classtools

    class Base:
        def some_method(self) -> None: ...

        @property
        def some_property(self) -> int: ...
        
        @some_property.setter
        def some_property(self, value) -> None: ...
        
        @some_property.deleter
        def some_property(self) -> None: ...
    
    @classtools.class_override
    class Child(Base):
        
        @classtools.method_override
        def some_method(self, some_value) -> None: ... # This is valid

        @classtools.method_override
        def some_other_method(self) -> None: ... # This is invalid

        @property
        def some_property(self) -> str: ...  # overloaded property
        # This property has no setter or deleter defined here
        # It will use the Base's setter and deleter.
    ```

    #### Extra Features and Working:

    `classtools.class_override` looks for the methods and propeties in
    the recent or direct parent of the child class.

    To look at the top most, class for methods and properties,
    `classtools.look_in` can be used to set the default lookup.

    By default it is set to `'recent'`.

    Example:

    ```python
    from modstore.tools import classtools

    # At this point, defaut lookup is `recent`

    class Top:
        def some_method(self) -> None: ...
    
    @classtools.class_override
    class Mid(Top):
        
        @classtools.method_override
        def some_method(self) -> str: ...

        def some_other_method(self) -> None: ...
    
    # still lookup is `recent`

    @classtools.class_override
    class Bottom(Mid):
        
        @classtools.method_override
        def some_method(self) -> int: ...

        @classtools.method_override
        def some_other_method(self) -> str: ... # This is valid.
    ```

    However, if the lookup is set to `topmost` (can take only `topmost`
    or `recent`) as values.

    ```python
    from modstore.tools import classtools

    classtools.look_in('topmost')
    # This can be done in any point of time.

    class Top:
        def some_method(self) -> None: ...
    
    @classtools.class_override
    class Mid(Top):
        
        @classtools.method_override
        def some_method(self) -> str: ...
        # This is valid as the top most class (Top) has a method
        # named some_method

        def some_other_method(self) -> None: ...
    
    @classtools.class_override
    class Bottom(Mid):
        
        @classtools.method_override
        def some_method(self) -> int: ...

        @classtools.method_override
        def some_other_method(self) -> str: ... # This is invalid.
        # The topmost class `Top` does not have any method named
        # some_other_method.
    ```

    For default and general usage, do not change lookup for convenience.
    """

    @classmethod
    def look_in(cls, baseclass: Literal['topmost', 'recent'] = 'recent') -> None:
        """Change the default lookup.
        
        `classtools.class_override` looks for the methods and propeties in
        the recent or direct parent of the child class.

        To look at the top most, class for methods and properties,
        `classtools.look_in` can be used to set the default lookup.

        By default it is set to `'recent'`.

        Example:

        ```python
        from modstore.tools import classtools

        # At this point, defaut lookup is `recent`

        class Top:
            def some_method(self) -> None: ...
        
        @classtools.class_override
        class Mid(Top):
            
            @classtools.method_override
            def some_method(self) -> str: ...

            def some_other_method(self) -> None: ...
        
        # still lookup is `recent`

        @classtools.class_override
        class Bottom(Mid):
            
            @classtools.method_override
            def some_method(self) -> int: ...

            @classtools.method_override
            def some_other_method(self) -> str: ... # This is valid.
        ```

        However, if the lookup is set to `topmost` (can take only `topmost`
        or `recent`) as values.

        ```python
        from modstore.tools import classtools

        classtools.look_in('topmost')
        # This can be done in any point of time.

        class Top:
            def some_method(self) -> None: ...
        
        @classtools.class_override
        class Mid(Top):
            
            @classtools.method_override
            def some_method(self) -> str: ...
            # This is valid as the top most class (Top) has a method
            # named some_method

            def some_other_method(self) -> None: ...
        
        @classtools.class_override
        class Bottom(Mid):
            
            @classtools.method_override
            def some_method(self) -> int: ...

            @classtools.method_override
            def some_other_method(self) -> str: ... # This is invalid.
            # The topmost class `Top` does not have any method named
            # some_other_method.
        ```

        For default and general usage, do not change lookup for convenience.
        """
        ...
    
    @staticmethod
    def class_override(cls: Type[CLASS]) -> Type[CLASS]:
        """Override decorator for Child Class.
        
        `class_override` is a decorator for `class` objects and
        should be used only on classes that are inheriting some
        other base class. On classes, that do not inherit any other
        base class it will do nothing.

        While using `class_override`, if the child class has properties
        that are overloaded, and either `fset` or `fdel` or both are not
        defined in the child class, `class_override` will make the child
        class use the base class's `fdel` and `fset`.

        Additionally, if any method found in the child class has an
        `__override__` attribute set to True (as a result of
        `method_override` decorator), It will check if the base class has
        that method or not, if not, it will raise `MethodOverrideError`
        (ultimately contributing towards maintaing large code bases (as
        it was for `typing.override`)).

        It will also check, any method having `method_override` decorator
        belongs to a class that is a child class of some other parent class
        or not. If found it is not, `MethodOverrideError` will be raised.

        The methods or properties that are not explicitly defined in the child
        class, will be taken from the base class (no contribution here).
        """
        ...
    
    @staticmethod
    def method_override(definition: Callable[..., METHOD]) -> Callable[..., METHOD]:
        """Override decorator for methods.

        `method_override` sets the `__override__` attribute of any
        method it is decorated on top of, as True.
        """
        ...

class BooleanError(Exception):
    """Generic Exception class for Boolean errors."""
    ...

class CustomBoolean(ABC):
    @abstractmethod
    def __init__(self, parent: Any, attribute: str, value: Any) -> None:
        """`CustomBoolean` definition class.
        
        This is a custom boolean class that acts as boolean
        but can also have several custom methods into it.
        """
        ...
    
    @abstractmethod
    def __bool__(self) -> bool:
        """Implementation of boolean behaviour."""
        ...
    
    @abstractmethod
    def __call__(self) -> Any:
        """Return the actual undelying value."""
        ...

    @abstractmethod
    def __set__(self, instance: CLASS, value: Any) -> None:
        """Sets the value in the original parent class and in self."""

    @abstractmethod
    def __delete__(self, instance: CLASS) -> None:
        """Deletes the attribute in the original parent class and in self."""
    
    def error(self, *args: Any) -> BooleanError:
        """Returns BooleanError with provided args."""
        ...

Error = TypeVar('Error')

class Property:
    """Dynamic Property Generator class.
    
    This class can be used to dynamically generate properties. However,
    this is completely different than built-in `property` class.

    In a code file (`.py`):
    ```python
    class SomeClass:
        def __init__(self, value) -> None:
            self.value = value
        
        content = Property(attribute='value')
        # this is the `Dynamic Property Generator`
    ```

    #### OR

    ```python
    class SomeClass:
        def __init__(self, value) -> None:
            self.value = value
        
        content = Property(getter=lambda self: self.value is not None)
    ```

    In a stub file (`.pyi`):
    ```python
    class SomeClass:
        
        content: property
        # Note that this is built-in `property` class.

        def __init__(self, value: any) -> None: ...
    ```

    #### OR

    ```python
    class SomeClass:
        def __init__(self, value: any) -> None: ...
        @property
        def content(self) -> any:
            \"\"\"docstring here.\"\"\"
            ...
    ```

    This practice will help with the static type checkers as `Property`
    class is not supported and is an externally provided feature.
    """
    @overload
    def __init__(
            self,
            *,
            attribute: str,
            setter: bool = False,
            deleter: bool = False,
            error: Error = None,
            doc: Union[str, None] = None,
            default: Any = None,
            _setter_error_arguments: Tuple[Any] = (),
            _deleter_error_arguments: Tuple[Any] = (),
            _deleter_deletes_attribute: bool = False,
    ) -> None:
        """Create a custom `property` object that automatically generates
        setter and deleter based on parameters.
        
        #### Parameter Description

        - `attribute` accepts the attribute name to be accessed from the class.
        
        - set `setter` to `True` to allow the property to be set by user, else,
            it will raise `error` with `_setter_error_arguments`.

        - set `deleter` to `True` to allow the property to be deleted (if the
            `_deleter_deletes_attribute` is `True`) or assigned to None (if the
            `_deleter_deletes_attribute` is `False`), else, it will raise `error`
            with `_deleter_error_arguments`.

        - `doc` sets the docstring for the property.

        - `default` is the default value to be returned if the `attribute` does
            not exist.
        """
        ...
    @overload
    def __init__(
            self,
            *,
            getter: Callable[[Any], Any],
            setter: Union[Callable[[Any, Any], None], None] = None,
            deleter: Union[Callable[[Any], None], None] = None,
            error: Error = None,
            doc: Union[str, None] = None,
            _setter_error_arguments: Tuple[Any] = (),
            _deleter_error_arguments: Tuple[Any] = (),
    ) -> None:
        """Create a custom `property` object that automatically generates
        setter and deleter based on parameters.
        
        #### Parameter Description

        - `getter` defines the logic for accessing the property.

            ```python
            class SomeClass:
                def __init__(self, value):
                    self.value = value
                
                isNone = Property(getter=lambda self: self.value is None)
            ```
        - if `setter` is not provided, it will be set to None, if provided,
            the setter will be set to the provided logic.

            ```python
            class SomeClass:
                def __init__(self, value):
                    self.value = value
                
                isNone = Property(
                    getter=lambda self: self.value,
                    setter=lambda self, value: self.value = value,
                )
            ```
        - the `deleter` works the same way as `setter`.

            ```python
            class SomeClass:
                def __init__(self, value):
                    self.value = value
                
                isNone = Property(
                    getter=lambda self: self.value,
                    setter=lambda self, value: self.value = value,
                    deleter=lambda self: del self.value,
                )
            ```
        - If `error` is provided and if `setter` or `deleter` or both are
            `None`, they will be raise the provided `error` with either
            `_setter_error_arguments` or `_deleter_error_arguments`.
        """
        ...
    
    def __get__(self, instance: CLASS, owner: Type[Any]) -> Any: ...
    def __set__(self, instance: CLASS, value: Any) -> None: ...
    def __delete__(self, instance: CLASS) -> None: ...
    def __docstring__(self) -> Union[str, None]: ...