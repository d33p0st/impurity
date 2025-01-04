from typing import (
    Any,
    Mapping,
    TypeVar,
    Dict,
    Generic,
    Union,
    overload,
    List as basicList,
    Tuple,
    Set,
    Iterable,
    Type,
    Callable,
    Iterator,
    Literal
)
from collections.abc import KeysView, ValuesView, ItemsView
from collections import defaultdict, Counter
from ..exceptions import HashMapError
import pickle
import hashlib
import sys

K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')

class hashmap_keys(KeysView, Generic[K]):
    def __init__(self, mapping: Mapping[K, V]) -> None:
        self._mapping = mapping
        self._keys = list(self._mapping.keys())
    
    def __iter__(self) -> Iterator[K]:
        return iter(self._keys)
    
    def __contains__(self, key: object) -> bool:
        return key in self._keys
    
    def __len__(self) -> int:
        return len(self._keys)
    
    def __str__(self) -> str:
        data = [f"{x}: _" for x in self._mapping]
        return "hashmap_keys({" + ', '.join(data) + "})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __getitem__(self, index: int) -> K:
        return self._keys[index]

class hashmap_values(ValuesView, Generic[V]):
    def __init__(self, mapping: Mapping[K, V]) -> None:
        self._mapping = mapping
        self._values = list(self._mapping.values())
    
    def __iter__(self) -> Iterator[V]:
        return iter(self._values)
    
    def __contains__(self, value: object) -> bool:
        return value in self._values
    
    def __len__(self) -> int:
        return len(self._values)
    
    def __str__(self) -> str:
        data = [f"_: {x}" for x in self._mapping.values()]
        return "hashmap_values({" + ", ".join(data) + "})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __getitem__(self, index: int) -> V:
        return self._values[index]

class hashmap_items(ItemsView, Generic[K, V]):
    def __init__(self, mapping: Mapping[K, V]) -> None:
        self._mapping = mapping
        self._items = list(self._mapping.items())
    
    def __iter__(self) -> Iterator[Tuple[K, V]]:
        return iter(self._items)
    
    def __contains__(self, item: Tuple[Any, Any]) -> bool:
        return item in self._items
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __str__(self) -> str:
        return f"hashmap_items({self._mapping})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __getitem__(self, index: int) -> Tuple[K, V]:
        return self._items[index]

class hashmap_internal_object(Generic[K, V]):
    ALLOWED = (Mapping, Dict, Counter, defaultdict)

    def __init__(self, innerobj, default = None):
        if not isinstance(innerobj, self.ALLOWED):
            raise TypeError(f"hashmap_internal_object only accepts {self.ALLOWED} types. Provided: {type(innerobj)}")
        self._internal = innerobj
        self._default = default if default else None
    
    
    @property
    def object(self):
        return self._internal
    
    @object.setter
    def object(self, object) -> None:
        if not isinstance(object, self.ALLOWED):
            raise TypeError(f"hashmap_internal_object only accepts {self.ALLOWED} types. Provided: {type(object)}")
        self._internal = object
    
    @object.deleter
    def object(self) -> None:
        del self._internal
    
    @property
    def ifdefault(self) -> bool:
        return self._default is not None
    
    @ifdefault.setter
    def ifdefault(self, obj) -> None:
        raise HashMapError("'ifdefault' property cannot be manually set for hashmap_internal_object.")
    
    @ifdefault.deleter
    def ifdefault(self) -> None:
        raise HashMapError("'ifdefault' property cannot be deleted manually for hashmap_internal_object.")
    
    def __str__(self) -> str:
        return str(dict(self._internal))
    
    def __repr__(self) -> str:
        return repr(dict(self._internal))

class HashMap(Generic[K, V]):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, *, default: Callable[[], V]) -> None: ...
    @overload
    def __init__(self, object: Union[Dict[K, V], Mapping[K, V]]) -> None: ...
    @overload
    def __init__(self, object: Iterable[Tuple[K, V]]) -> None: ...
    @overload
    def __init__(self, object: str) -> None: ...
    @overload
    def __init__(self, object: int) -> None: ...
    @overload
    def __init__(self, object: bytes) -> None: ...
    @overload
    def __init__(self, object: Iterable[K], *, default: Callable[[], V]) -> None: ...

    def __init__(self, object: Union[Any, None] = None, *, default: Union[Callable[[], V], None] = None) -> None:
        self._default: Union[Callable[[], V], None] = None

        if object is None and default is None:
            # Default with no params
            self._inner = hashmap_internal_object({})
        elif object is not None and default is None:
            # If Object is present, default is not
            # The Dict and Mapping - and the iterable[tuple] composition
            if isinstance(object, Mapping) or isinstance(object, dict) or self._check_iterable_tuple_composition(object):
                self._inner = hashmap_internal_object(dict(object))
            
            # str, int
            elif isinstance(object, str):
                self._inner = hashmap_internal_object(Counter(object))
            
            elif isinstance(object, int):
                dummy = Counter(str(object))
                dummy2 = {}
                for k, v in dummy.items():
                    dummy2[int(k)] = v
                
                self._inner = hashmap_internal_object(Counter(dummy2))
            
            elif isinstance(object, bytes):
                try:
                    unpacked_class: HashMap[K, V] = pickle.loads(object)
                except pickle.UnpicklingError:
                    raise HashMapError("Cannot UnPack HashMap from bytes.")
                except Exception as e:
                    raise HashMapError(f"UnPack Error: {e}")
                
                self._inner = hashmap_internal_object({})
                # update current hashmap based on the unpacked one.
                for k, v in unpacked_class.iter():
                    self[k] = v
            
            # Else parameter error
            else:
                raise HashMapError("Parameter Error - re-check params when calling HashMap(...)")

        elif object is None and default is not None:
            # Only default is present.
            self._inner = hashmap_internal_object(defaultdict(default))
        elif object is not None and default is not None:
            # If both object and default is present
            # it is of the type iterable[k]
            self._inner = hashmap_internal_object(defaultdict(default, {x: default() for x in object}))
        else:
            raise HashMapError("Parameter Error - re-check params when calling HashMap(...)")

        return None
        
    def _check_iterable_tuple_composition(self, iterable: Any) -> bool:
        # If iterable and not str
        if isinstance(iterable, Iterable) and not isinstance(iterable, str):
            # Iterate and check if all values are tuple and have only two values.
            for x in iterable:
                if not isinstance(x, tuple):
                    return False # false if not a tuple
                
                try: # try to get len. Might not support len op
                    if len(x) != 2:
                        return False # false if len not equal to 2
                except Exception:
                    return False # false if len not supported.
                
            return True # true if the loop exits
        else:
            return False # false if not iterable
    
    def __str__(self) -> str:
        return f"HashMap({self._inner})"
    
    def __repr__(self) -> str:
        return f"HashMap({repr(self._inner)})"
    
    def __getitem__(self, key: K) -> V:
        return self._inner.object[key]
    
    def __setitem__(self, key: K, value: V) -> None:
        self._inner.object[key] = value
        return None
    
    def __delitem__(self, key: K) -> None:
        del self._inner.object[key]
        return None
    
    def __iter__(self) -> Iterator[K]:
        return self.iterkeys().__iter__()
    
    def __len__(self) -> int:
        return len(self._inner.object)
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, HashMap):
            return self._inner.object == other._inner.object
        return self._inner.object == other
    
    @overload
    def iter(self) -> hashmap_items[K, V]: ...
    @overload
    def iter(self, step: int = 1, /) -> hashmap_items[K, V]: ...
    
    def iter(self, step: int = 1) -> hashmap_items[K, V]:
        if step == 1:
            return hashmap_items(self._inner.object)
        elif step <= 0:
            raise HashMapError("Cannot Iterate. an infinite loop or backward indexing might be present.")
        else:
            new_data = HashMap()
            current = list(self.iter())
            for i in range(0, len(current), step):
                new_data[current[i][0]] = current[i][1]
            
            return hashmap_items(new_data._inner.object)

    @overload
    def iterkeys(self) -> hashmap_keys[K]: ...
    @overload
    def iterkeys(self, step: int = 1, /) -> hashmap_keys[K]: ...
    
    def iterkeys(self, step: int = 1, /) -> hashmap_keys[K]:
        if step == 1:
            return hashmap_keys(self._inner.object)
        elif step <= 0:
            raise HashMapError("Cannot Iterate. an infinite loop or backward indexing might be present.")
        else:
            new_data = HashMap()
            current = list(self.iter())
            for i in range(0, len(current), step):
                new_data[current[i][0]] = current[i][1]
            
            return hashmap_keys(new_data._inner.object)
    
    @overload
    def itervalues(self) -> hashmap_values[V]: ...
    @overload
    def itervalues(self, step: int = 1, /) -> hashmap_values[V]: ...
    
    def itervalues(self, step: int = 1, /) -> hashmap_values[V]:
        if step == 1:
            return hashmap_values(self._inner.object)
        elif step <= 0:
            raise HashMapError("Cannot Iterate. an infinite loop or backward indexing might be present.")
        else:
            new_data = HashMap()
            current = list(self.iter())
            for i in range(0, len(current), step):
                new_data[current[i][0]] = current[i][1]
        
        return hashmap_values(new_data._inner.object)

    def invert(self) -> 'HashMap[V, Union[K, basicList[K]]]':
        inverted: Dict[V, Union[K, basicList[K]]] = {}
        for k, v in self.iter():
            if v in inverted:
                if isinstance(inverted[v], list):
                    inverted[v].append(k)
                else:
                    inverted[v] = [inverted[v], k]
            else:
                inverted[v] = k
        return HashMap(inverted)
    
    @overload
    def get(self, key: K, /) -> V: ...
    @overload
    def get(self, key: K, *, default: Union[V, Any, None] = None) -> Union[V, Any, None]: ...

    def get(self, key: K, **kwargs):
        if key in self:
            return self[key]
        else:
            if 'default' in kwargs:
                return kwargs['default']
            else:
                raise HashMapError(f"Key({key}) not found in HashMap.")
    
    def clear(self) -> None:
        return self._inner.object.clear()
    
    @property
    def length(self) -> int:
        return len(self._inner.object)
    
    @length.setter
    def length(self, _obj: Any) -> None:
        raise HashMapError("HashMap length property cannot be altered.")
    
    @length.deleter
    def length(self) -> None:
        raise HashMapError("HashMap length cannot be deleted.")
    
    @overload
    def update_using(self, other: 'HashMap[K, V]') -> None: ...
    @overload
    def update_using(self, other: Union[Mapping[K, V], Dict[K, V]]) ->  None: ...
    @overload
    def update_using(self, other: Iterable[Tuple[K, V]]) -> None: ...

    def update_using(self, other: Union[Mapping[K, V], Dict[K, V], 'HashMap[K, V]', Iterable[Tuple[K, V]]]) -> None:
        if isinstance(other, Iterable) and self._check_iterable_tuple_composition(other):
            # If Iterable[Tuple[K, V]]
            for key, value in other:
                self[key] = value
        elif isinstance(other, dict) or isinstance(other, Mapping):
            for key, value in other.items():
                self[key] = value
        
        elif isinstance(other, HashMap):
            for key, value in other.iter():
                self[key] = value
        else:
            raise HashMapError(f"Object Type {type(other)} not supported.")
    
    def flatten(self) -> bytes:
        return pickle.dumps(self)
    
    def setdefault(self, key: K, default: Callable[[], V], /) -> None:
        if key in self.iterkeys():
            raise HashMapError(f"Key '{key}' already present in HashMap.")
        
        self[key] = default()

class _hasher:
    def __init__(self, hashf: Literal['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'] = 'md5') -> None:
        if hashf == 'md5':
            self._function = hashlib.md5
        elif hashf == 'sha1':
            self._function = hashlib.sha1
        elif hashf == 'sha224':
            self._function = hashlib.sha224
        elif hashf == 'sha256':
            self._function = hashlib.sha256
        elif hashf == 'sha384':
            self._function = hashlib.sha384
        elif hashf == 'sha512':
            self._function = hashlib.sha512
        else:
            raise ValueError(f"_hasher un-supported hashf: {hashf}")
        
    def hash(self, object: object) -> str:
        return self._function(pickle.dumps(object))

class AutoHashMap(Generic[K, E]):
    SUPPORTED_HASH = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, *, create_from: Iterable[E]) -> None: ...
    @overload
    def __init__(self, *, create_from: Iterable[E], hash_function: Callable[[E], K]) -> None: ...
    @overload
    def __init__(self, *, create_from: Iterable[E], hash_function: Literal['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']) -> None: ...

    def __init__(self, *, create_from: Union[Iterable[E], None] = None, hash_function: Union[Callable[[E], K], Literal['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'], None] = None):
        self._inner: hashmap_internal_object[K, Union[E, basicList[E]]] = hashmap_internal_object({})
        self._function: Union[_hasher, Callable[[E], K], None] = None
        
        if create_from:
            if hash_function is not None and isinstance(hash_function, str):
                if hash_function not in self.SUPPORTED_HASH:
                    raise HashMapError(f"Parameter 'hash_function' can either be {self.SUPPORTED_HASH} or a callable.")
                
                # store function
                self._function = _hasher(hash_function)
                
                for x in create_from:
                    self._adder(self._function.hash(x), x)
                
            elif hash_function is not None and isinstance(hash_function, Callable):
                self._function = hash_function
                for x in create_from:
                    self._adder(self._function(x), x)
            else:
                self._function = _hasher()
                # hash function not provided
                for x in create_from:
                    self._adder(_hasher().hash(x), x)
    
    def _adder(self, key: K, value: E) -> None:
        if key in self:
            if isinstance(self._inner.object[key], list):
                self._inner.object[key].append(value)
            else:
                self._inner.object[key] = [self._inner.object[key], value]
        else:
            self._inner.object[key] = value
    
    def __iter__(self) -> Iterator[E]:
        return self.itervalues().__iter__()
    
    def __contains__(self, item: E) -> bool:
        return item in self._get_flattened_values()
    
    def _get_flattened_values(self) -> hashmap_values[E]:
        all_v = []
        for x in self.itervalues():
            if isinstance(x, list):
                all_v.extend(x)
            else:
                all_v.append(x)
        
        dummy = {}
        i = 0
        for x in all_v:
            dummy[i] = x
            i += 1
        
        return hashmap_values(dummy)
    
    def __str__(self) -> str:
        return f"AutoHashMap({self._inner})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def insert(self, value: E) -> None:
        if self._function is None:
            raise HashMapError("Hash Function is not set. Set it using 'set_hashf' method.")
        
        if isinstance(self._function, _hasher):
            self._adder(self._function.hash(value), value)
        elif isinstance(self._function, Callable):
            self._adder(self._function(value), value)
        else:
            raise HashMapError("UnKnown Error. Perhaps, the _function variable was modified.")
    
    @overload
    def set_hashf(self, function: Callable[[E], K]) -> None: ...
    @overload
    def set_hashf(self, function: Literal['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']) -> None: ...

    def set_hashf(self, function: Union[Callable[[E], K], Literal['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']]) -> None:
        old_function = self._function
        if isinstance(function, str):
            if function not in self.SUPPORTED_HASH:
                raise HashMapError(f"Parameter 'hash_function' can either be {self.SUPPORTED_HASH} or a callable.")
            self._function = _hasher(function)
        else:
            self._function = function
        
        self._update_according_to_function(old_function, self._function)
    
    def _check_list_hash(self, hash: str, to_check: basicList[Any], func: Callable[[E], K]) -> bool:
        for element in to_check:
            if func(element) != hash:
                return False
        
        return True
    
    def _update_list(self, _hasher: Callable, values: basicList[Any], to_update: Dict) -> None:
        for element in values:
            _hash = _hasher(element)

            if _hash in to_update:
                if isinstance(to_update[_hash], basicList):
                    to_update[_hash].append(element)
                else:
                    to_update[_hash] = [to_update[_hash], element]
            else:
                to_update[_hash] = element
        
        return None

    def _update_according_to_function(self, old_function: Union[_hasher, Callable[[E], K], None], new_function: Union[_hasher, Callable[[E], K]]) -> None:
        if old_function is not None:
            new_data = {}
            for value in self.itervalues():
                if isinstance(value, list):
                    if isinstance(new_function, _hasher):
                        # This is a list, all the values might not have
                        # the same hash values now that the function is 
                        # changed.
                        _hash_of_one = new_function.hash(value[0])

                        if self._check_list_hash(_hash_of_one, value, new_function.hash):
                            new_data[_hash_of_one] = value
                        else:
                            self._update_list(new_function.hash, value, new_data)
                            
                    elif isinstance(new_function, Callable):
                        _hash_of_one = new_function(value[0])
                        if self._check_list_hash(_hash_of_one, value, new_function):
                            new_data[_hash_of_one] = value
                        else:
                            self._update_list(new_function, value, new_data)
                else:
                    if isinstance(new_function, _hasher):
                        _hash_of_one = new_function.hash(value)
                        if _hash_of_one not in new_data:
                            new_data[_hash_of_one] = value
                        else:
                            if isinstance(new_data[_hash_of_one], basicList):
                                new_data[_hash_of_one].append(value)
                            else:
                                new_data[_hash_of_one] = [new_data[_hash_of_one], value]
                        
                    elif isinstance(new_function, Callable):
                        _hash_of_one = new_function(value)
                        if _hash_of_one not in new_data:
                            new_data[_hash_of_one] = value
                        else:
                            if isinstance(new_data[_hash_of_one], basicList):
                                new_data[_hash_of_one].append(value)
                            else:
                                new_data[_hash_of_one] = [new_data[_hash_of_one], value]
            
            if len(new_data) > 0:
                self._inner: hashmap_internal_object[K, Union[E, basicList[E]]] = hashmap_internal_object(new_data)
    
    def get_hashf(self) -> Union[Callable[[E], K], None]:
        if self._function is None:
            return None
        
        if isinstance(self._function, _hasher):
            return self._function.hash
        
        if isinstance(self._function, Callable):
            return self._function

    @overload
    def iter(self) -> hashmap_items[K, Union[E, basicList[E]]]: ...
    @overload
    def iter(self, step: int = 1, /) -> hashmap_items[K, Union[E, basicList[E]]]: ...

    def iter(self, step: int = 1, /) -> hashmap_items[K, Union[E, basicList[E]]]:
        if step == 1:
            return hashmap_items(self._inner.object)
        elif step <= 0:
            raise HashMapError("Cannot Iterate. an infinite loop or backward indexing might be present.")
        else:

            if len(self._inner.object) == 0:
                return hashmap_items({})
            
            current = list(self.iter())
            new_data_values: basicList[E] = []
            for i in range(0, len(current), step):
                new_data_values.append(current[i][1]) # values
            
            if isinstance(self._function, _hasher):
                return hashmap_items(AutoHashMap(create_from=new_data_values, hash_function=self._function.hash)._inner.object)
            elif isinstance(self._function, Callable):
                return hashmap_items(AutoHashMap(create_from=new_data_values, hash_function=self._function)._inner.object)
            else:
                # self._function is None
                # self._function is only none when len is 0 (handled above, will never happen)
                return hashmap_items({})
    
    @overload
    def iterkeys(self) -> hashmap_keys[K]: ...
    @overload
    def iterkeys(self, step: int = 1, /) -> hashmap_keys[K]: ...

    def iterkeys(self, step: int = 1, /) -> hashmap_keys[K]:
        if step == 1:
            return hashmap_keys(self._inner.object)
        elif step <= 0:
            raise HashMapError("Cannot Iterate. an infinite loop or backward indexing might be present.")
        else:
            
            if len(self._inner.object) == 0:
                return hashmap_keys({})
            
            current = list(self.iter())
            new_data: Dict[K, E] = {}
            for i in range(0, len(current), step):
                new_data[current[i][0]] = current[i][1]
            
            return hashmap_keys(new_data)
    
    @overload
    def itervalues(self) -> hashmap_values[Union[E, basicList[E]]]: ...
    @overload
    def itervalues(self, step: int = 1, /) -> hashmap_values[Union[E, basicList[E]]]: ...

    def itervalues(self, step: int = 1, /) -> hashmap_values[Union[E, basicList[E]]]:
        if step == 1:
            return hashmap_values(self._inner.object)
        elif step <= 0:
            raise HashMapError("Cannot Iterate. an infinite loop or backward indexing might be present.")
        else:

            if len(self._inner.object) == 0:
                return hashmap_values({})
            
            current = list(self.iter())
            new_data = Dict[K, E] = {}
            for i in range(0, len(current), step):
                new_data[current[i][0]] = current[i][1]
            
            return hashmap_values(new_data)
    
    def pop(self, value: E) -> Union[K, None]:
        for k, v in self.iter():
            if isinstance(v, list) and value in v:
                self._inner.object[k].remove(value)
                if len(self._inner.object[k]) == 1:
                    self._inner.object[k] = self._inner.object[k][0]
                return k
            elif v == value:
                del self._inner.object[k]
                return k
        return None
    
    def getitems(self) -> basicList[Tuple[K, Union[E, basicList[E]]]]:
        return list(self.iter())
    
    def getkeys(self) -> basicList[K]:
        return list(self.iterkeys())

    def getvalues(self, *, flatten: bool = False) -> basicList[Union[E, basicList[E]]]:
        if not flatten:
            return list(self.itervalues())
        else:
            return list(self._get_flattened_values())