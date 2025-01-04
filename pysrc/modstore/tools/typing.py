
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
    _look_in: Literal['topmost', 'recent'] = 'recent'

    @classmethod
    def look_in(cls, baseclass: Literal['topmost', 'recent'] = 'recent'):
        cls._look_in = baseclass

    @staticmethod
    def class_override(cls: Type[CLASS]) -> Type[CLASS]:

        # For all members
        for name, member in inspect.getmembers(cls):

            # Handling missing property methods.
            if isinstance(member, property):

                # Try to find the property of current class
                # in base class, if no base class, exit.

                try:
                    all_bases = cls.__bases__
                except AttributeError:
                    continue

                if classtools._look_in == 'recent':
                    try:
                        base_member: Optional[property] = getattr(cls.__bases__[0], name)
                    except (IndexError, AttributeError):
                        continue
                elif classtools._look_in == 'topmost':
                    if not all_bases:
                        continue
                    
                    base = all_bases[0]
                    while all_bases:
                        base = all_bases[0]
                        try:
                            all_bases = base.__bases__
                            if all_bases[0] is object:
                                break
                        except AttributeError:
                            break
                    
                    try:
                        base_member: Union[property, None] = getattr(base, name)
                    except AttributeError:
                        continue
                
                # if property found in base class.
                if isinstance(base_member, property):
                    # if the setter of the property in current class
                    # is not set, but found in base class, use it.
                    if member.fset is None and base_member.fset is not None:
                        new_property = property(
                            fget=member.fget,
                            fset=base_member.fset,
                            fdel=member.fdel if member.fdel is not None else base_member.fdel,
                            # use base memeber's fdel if fdel is also not there.
                        )
                        setattr(cls, name, new_property)
                    
                    # if the deleter for the property in current class
                    # is not set, but found in base class, use it.
                    if member.fdel is None and base_member.fdel is not None:
                        new_property = property(
                            fget=member.fget,
                            fset=member.fset if member.fset is not None else base_member.fset,
                            # use base member's fset if member's is not present.
                            fdel=base_member.fdel
                        )
                        setattr(cls, name, new_property)
            elif inspect.isfunction(member) and hasattr(member, '__override__') and getattr(member, '__override__') == True:
                
                # At this point of time, the method is found to be
                # set as override.

                try:
                    all_bases = cls.__bases__
                except AttributeError:
                    # Case: No base class found but method is overriden
                    error = "{} method is found to be overriden but no base class found for {}"
                    raise MethodOverrideError(error, name, cls.__name__)

                if classtools._look_in == 'recent':
                    try:
                        base_method: Union[function, None] = getattr(cls.__bases__[0], name)
                    except AttributeError:
                        # Case: Base class is present but no method of such name found in the base class.
                        # and the method is overriden
                        error = "{} method is found to be overriden but no such method is found in the base class of {}. base_class_considered: {}"
                        raise MethodOverrideError(error, name, cls.__name__, cls.__bases__[0].__name__)

                    # Case: If found, do nothing. Only errors are captured here.
                elif classtools._look_in == 'topmost':

                    if not all_bases:
                        # method found but no base class.
                        error = "{} method is found to be overriden but no base class found for {}"
                        raise MethodOverrideError(error, name, cls.__name__)
                    
                    base = None
                    while all_bases:
                        base = all_bases[0]
                        try:
                            all_bases = base.__bases__
                            if all_bases[0] is object:
                                break
                        except AttributeError:
                            break
                    
                    try:
                        base_method: Optional[function] = getattr(base, name)
                    except AttributeError:
                        error = "{} method is found to be overriden but no such method is found in the base class of {}. base_class_considered: {}"
                        raise MethodOverrideError(error, name, cls.__name__, base.__name__)


        return cls

    @staticmethod
    def method_override(definition: Callable[..., METHOD]) -> Callable[..., METHOD]:
        setattr(definition, '__override__', True)
        return definition

class functiontools:
    ...

class BooleanError(Exception):
    pass

class CustomBoolean(ABC):
    @abstractmethod
    def __init__(self, parent: Any, attribute: str, value: Any) -> None:
        pass

    @abstractmethod
    def __bool__(self) -> bool:
        pass

    @abstractmethod
    def __call__(self) -> Any:
        pass

    @abstractmethod
    def __set__(self, instance: CLASS, value: Any) -> None:
        pass

    @abstractmethod
    def __delete__(self, instance: CLASS) -> None:
        pass
    
    def error(self, *args: Any):
        return BooleanError(*args)

Error = TypeVar('Error')

class Property:
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
    ) -> None: ...
    @overload
    def __init__(
            self,
            *,
            getter: Callable[[Any], Any],
            setter: Union[Callable[[Any, Any], None]] = None,
            deleter: Union[Callable[[Any], None]] = None,
            error: Error = None,
            doc: Union[str, None] = None,
            _setter_error_arguments: Tuple[Any] = (),
            _deleter_error_arguments: Tuple[Any] = (),
    ) -> None: ...

    def __init__(
            self,
            *,
            attribute: Union[str, None] = None,
            getter: Union[Callable[[Any], Any], None] = None,
            setter: Union[bool, Callable[[Any, Any], None], None] = False,
            deleter: Union[bool, Callable[[Any], None], None] = False,
            error: Error = None,
            doc: Union[str, None] = None,
            default: Any = None,
            _setter_error_arguments: Tuple[Any] = (),
            _deleter_error_arguments: Tuple[Any] = (),
            _deleter_deletes_attribute: bool = False,
    ) -> None:
        if getter is None: # treat it like a = Property(attribute='attrname')

            def _setter(cls, value) -> None: # default, sets the attribute
                setattr(cls, attribute, value)
                return None

            def _deleter(cls) -> None: # default, sets to None or deletes
                if _deleter_deletes_attribute:
                    delattr(cls, attribute)
                else:
                    setattr(cls, attribute, None)
                return None
        
            if error is not None: # if error is provided.
                if isinstance(setter, bool) and not setter: # if setter is set to false, raise error if called
                    def _setter(cls, value) -> None:
                        raise error(*_setter_error_arguments)
                if isinstance(deleter, bool) and not deleter: # if deleter is set to false, raise error if called
                    def _deleter(cls) -> None:
                        raise error(*_deleter_error_arguments)
        
            self.property = property(lambda cls: getattr(cls, attribute, default), _setter, _deleter, doc)
        
        elif isinstance(getter, Callable):
        # treat it like
        # a = Property(attribute = 'attrname', logic = lambda: name is not None )

            # logic is callable here,
            def _getter(cls) -> Any:
                return getter(cls)
            
            if isinstance(setter, Callable):
                _setter = setter
            else:
                _setter = None
            
            if isinstance(deleter, Callable):
                _deleter = deleter
            else:
                _deleter = None
            
            if error is not None:
                if setter is None or setter is False:
                    def _setter(cls, value) -> None:
                        raise error(*_setter_error_arguments)
                
                if deleter is None or deleter is False:
                    def _deleter(cls) -> None:
                        raise error(*_deleter_error_arguments)
            
            self.property = property(_getter, _setter, _deleter, doc)

        self.__doc__ = doc
        self.__error__ = error
    
    def __get__(self, instance: CLASS, owner: Type[Any]) -> Any:
        if instance is None:
            if self.__error__ is not None:
                raise self.__error__(f"Propeties cannot be accessed without initializing the class.")
            else:
                raise AttributeError(f"Propeties cannot be accessed without initializing the class.")
        return self.property.fget(instance)
    
    def __set__(self, instance: CLASS, value: Any) -> None:
        if instance is None:
            if self.__error__ is not None:
                raise self.__error__(f"Propeties cannot be accessed without initializing the class.")
            else:
                raise AttributeError(f"Propeties cannot be accessed without initializing the class.")
        return self.property.fset(instance, value)
    
    def __delete__(self, instance: CLASS) -> None:
        if instance is None:
            if self.__error__ is not None:
                raise self.__error__(f"Propeties cannot be accessed without initializing the class.")
            else:
                raise AttributeError(f"Propeties cannot be accessed without initializing the class.")
        return self.property.fdel(instance)
    
    def __docstring__(self) -> Union[str, None]:
        return self.__doc__