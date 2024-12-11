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

K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')

class hashmap_keys(KeysView, Generic[K]):
    """`HashMap Keys View Class.`
    
    View wrapper for HashMap Keys.

    - Iteration returns a list of keys.
    - length returns the length of list of keys.
    - str type casting is enabled. returns only keys, and values are ommited.
    - makes `hashmap.iterkeys()[::-1]` valid.
    """
    
    def __init__(self, mapping: Union[Mapping[K, V], Dict[K, V]]) -> None:
        """create a KeysView Object from a dict or mapping type data where
        only keys can be iterated."""
        ...

    def __iter__(self) -> Iterator[K]:
        """returns an Iterator over the Keys."""
        ...
    
    def __contans__(self, key: object) -> bool:
        """Enables the `in` keyword interaction over the Keys."""
        ...
    
    def __len__(self) -> int:
        """Number of Keys."""
        ...
    
    def __str__(self) -> str:
        """String format for Keys."""
        ...
    
    def __repr__(self) -> str:
        """repr() implementation."""
        ...
    
    def __getitem__(self, index: int) -> K: ...

class hashmap_values(ValuesView, Generic[V]):
    """`HashMap ValuesView Class.`
    
    View Wrapper for HashMap Values.

    - Iteration returns a list of values.
    - length returns the length of list of values.
    - str typecasting is enabled. returns only values, keys are ommitted.
    - makes `hashmap.itervalues()[::-1]` valid.
    """

    def __init__(self, mapping: Union[Mapping[K, V], Dict[K, V]]) -> None:
        """create a ValuesView Object from a dict or mapping type data where
        only values can be iterated."""
        ...

    def __iter__(self) -> Iterator[K]:
        """returns an Iterator over the Values."""
        ...
    
    def __contans__(self, key: object) -> bool:
        """Enables the `in` keyword interaction over the Values."""
        ...
    
    def __len__(self) -> int:
        """Number of Values."""
        ...
    
    def __str__(self) -> str:
        """String format for Values."""
        ...
    
    def __repr__(self) -> str:
        """repr() implementation."""
        ...
    
    def __getitem__(self, index: int) -> V: ...

class hashmap_items(ItemsView, Generic[K, V]):
    """`HashMap ItemsView Class.`
    
    View Wrapper for HashMap Items.

    - Iteration of a list of tuple[key, value].
    - Length returns the length of list of items.
    - str typecasting is enabled. returns both keys and values.
    - makes `hashmap.iter()[::-1]` valid.
    """

    def __init__(self, mapping: Union[Mapping[K, V], Dict[K, V]]) -> None:
        """create a ItemsView Object from a dict or mapping type data where
        both keys and values can be iterated."""
        ...

    def __iter__(self) -> Iterator[K]:
        """returns an Iterator over the (Keys, Values)."""
        ...
    
    def __contans__(self, key: object) -> bool:
        """Enables the `in` keyword interaction over the (Keys, Values)."""
        ...
    
    def __len__(self) -> int:
        """Number of items."""
        ...
    
    def __str__(self) -> str:
        """String format for items."""
        ...
    
    def __repr__(self) -> str:
        """repr() implementation."""
        ...
    
    def __getitem__(self, index: int) -> Tuple[K, V]: ...

class hashmap_internal_object(Generic[K, V]):
    """`Internal Data Store Object for HashMap.`
    
    - Stores the Internal object.
    - Could be of type: Mapping, Dict, Counter, defaultdict.
    - Other types are not supported.
    """

    ALLOWED: Tuple[type[Mapping], type[Dict], type[Counter], type[defaultdict]]
    _internal: Union[Mapping[K, V], Dict[K, V], Counter[K, V], defaultdict[K ,V]]
    _default: Union[Any, None]

    def __init__(self, innerobj: Union[Mapping[K, V], Dict[K, V], Counter[K, V], defaultdict[K ,V]], default: Union[Any, None] = None) -> None:
        """create a hashmap_internal_object."""
        ...
    
    @property
    def object(self) -> Union[Mapping[K, V], Dict[K, V], Counter[K, V], defaultdict[K ,V]]:
        """`the internal object '_internal'`"""
        ...
    
    @object.setter
    def object(self, object: Union[Mapping[K, V], Dict[K, V], Counter[K, V], defaultdict[K ,V]]) -> None: ...
    @object.deleter
    def object(self) -> None: ...

    @property
    def ifdefault(self) -> bool:
        """If default is set."""
        ...
    
    @ifdefault.setter
    def ifdefault(self, obj: Any) -> None: ...
    @ifdefault.deleter
    def ifdefault(self) -> None: ...

    def __str__(self) -> str:
        """str()"""
        ...
    
    def __repr__(self) -> str:
        """repr()"""
        ...

class HashMap(Generic[K, V]):
    """`HashMap Class`
    
    `HashMap` class revolutionizes the classic dictionary
    class of python and brings all necessary operations
    already in-built. Create dynamic HashMaps from a ton
    of sources and do time intensive tasks in one go.

    HashMap Creation Sources:
    - `Dict[Any, Any]` or `Mapping[Any, Any]`
    - `Iterable[Tuple[Any, Any]]`
    - `str` (count letters) (keys: letters, values: their counts)
    - `int` (count digits) (keys: digit, values: their counts)
    - `Empty Default Dict`: Define a default Value Type, Any keys
      added later will have the same default type (works like
      collections.defaultdict)
    - `Default Dict with pre-existing keys`: Create a default dict
      with some pre-existing list of keys.
    
    HashMap Access:
    - Accessible through square brackets (`[]`)
    - in-built methods.
    """

    _default: Union[Callable[[], V], None] = None
    _inner: hashmap_internal_object

    @overload
    def __init__(self) -> None:
        """Create an empty `HashMap`."""
        ...
    
    @overload
    def __init__(self, *, default: Callable[[], V]) -> None:
        """Create an empty `HashMap` with default value type.
        
        Example:
        ```python
        >>> from modstore import HashMap
        >>> hashmap = HashMap(default=list)
        >>> hashmap['A']
        []

        >>> hashmap
        HashMap({})

        >>> hashmap['A'].extend(['a', 'b'])
        >>> hashmap
        HashMap({'A': ['a', 'b']})
        ```
        """
        ...
    
    @overload
    def __init__(self, object: Union[Dict[K, V], Mapping[K, V]]) -> None:
        """Create a `HashMap` with pre-existing dict or mapping."""
        ...
    
    @overload
    def __init__(self, object: Iterable[Tuple[K, V]]) -> None:
        """Create a `HashMap` with an Iterable whose elements are in
        the form of Tuple. Each tuple must of length 2 where first
        element must be the key and the second element must be the
        value."""
        ...
    
    @overload
    def __init__(self, object: str) -> None:
        """Create a `HashMap` from a string. The `HashMap` will have
        letters for keys and their respective count as values."""
        ...
    
    @overload
    def __init__(self, object: int) -> None:
        """Create a `HashMap` from an int. The `HashMap` will have
        digits(int) for keys and their respective count as values."""
        ...
    
    @overload
    def __init__(self, object: bytes) -> None:
        """Create a `HashMap` from another flattened `HashMap`.
        
        Will raise `HashMapError` if unpacking fails or some
        random data is provided.
        """
        ...
    
    @overload
    def __init__(self, object: Iterable[K], *, default: Callable[[], V]) -> None:
        """Create a `HashMap` from an iterable which contains the keys,
        with default value type. This basically creates a `HashMap` with
        pre-existing keys with their values initialised as the default type.
        Any new keys added will also have the default value type."""
        ...
    
    # internal methods
    def _check_iterable_tuple_composition(self, iterable: Any) -> bool:
        """Internal method to check any variable, if it is in the form
        `Iterable[Tuple[K, V]]`."""
        ...
    
    def __str__(self) -> str:
        """Generate str(hashmap) functionality. Returns String."""
        ...
    
    def __repr__(self) -> str:
        """Generate String representation."""
        ...
    
    def __getitem__(self, key: K) -> V:
        """Make `HashMap` accessible using `[]`"""
        ...
    
    def __setitem__(self, key: K, value: V) -> None:
        """Make `HashMap` accessible using `[]`"""
        ...
    
    def __delitem__(self, key: K) -> None:
        """Make `HashMap` accessible using `[]`"""
        ...
    
    def __iter__(self) -> Iterator[K]:
        """Make Keys iterable using the `in` keyword."""
        ...
    
    def __len__(self) -> int:
        """Length of HashMap"""
        ...
    
    def __eq__(self, other: Any) -> bool:
        """Equality of objects."""
        ...

    # properties
    @property
    def length(self) -> int:
        """Get length of items."""
        ...
    
    # methods
    @overload
    def iter(self) -> hashmap_items[K, V]:
        """Method to iterate over a tuple of key-value pair.

        Works like `dict.items()`

        Example:
        ```python
        >>> from modstore import HashMap
        >>> h = HashMap([(1, 2), (3, 4)])
        >>> for key, value in h.iter():
        ...     print(key, value)
        ... 
        1 2
        3 4
        ```
        """
        ...
    
    @overload
    def iter(self, step: int = 1, /) -> hashmap_items[K, V]:
        """Method to iterate over a tuple of key-value pair.
        Supports `step` similar to `range()` function.
        
        Default for `step` is 1. i.e., increment index by
        one for moving next."""
        ...
    
    @overload
    def iterkeys(self) -> hashmap_keys[K]:
        """Method to iterate over a list of keys.

        Works like `dict.keys()`

        Example:
        ```python
        >>> from modstore import HashMap
        >>> h = HashMap([(1, 2), (2, 3)])
        >>> for key in h.iterkeys():
        ...     print(key)
        ...
        1
        2
        ```
        """
        ...
    
    @overload
    def iterkeys(self, step: int = 1, /) -> hashmap_keys[K]:
        """Method to iterate over a list of keys.
        Supports `step` similar to `range()` function.
        
        Default for `step` is 1. i.e., increment index by
        one for moving next.
        """
        ...
    
    @overload
    def itervalues(self) -> hashmap_values[V]:
        """Method to iterate over a list of values.
        
        Works like `dict.values()`

        Example:
        ```python
        >>> from modstore import HashMap
        >>> h = HashMap([(1, 2), (2, 3)])
        >>> for value in h.itervalues():
        ...     print(value)
        ...
        2
        3
        ```
        """
        ...
    
    @overload
    def itervalues(self, step: int = 1, /) -> hashmap_values[V]:
        """Method to iterate over a list of values.
        Supports `step` similar to `range()` function.
        
        Default for `step` is 1. i.e., increment index by
        one for moving next.
        """
        ...
    
    def invert(self) -> 'HashMap[V, Union[K, basicList[K]]]':
        """Invert the keys and values.
        
        if a value is present multiple times (for different keys)
        the value will be converted to key, with all the keys that
        were associated as a list of values.

        Example:
        ```python
        >>> from modstore import HashMap
        >>> h = HashMap({'a': 1, 'b': 1, 'c': 2, 'd': 4})
        >>> h
        HashMap({'a': 1, 'b': 1, 'c': 2, 'd': 4})

        >>> h.invert()
        HashMap({1: ['a', 'b'], 2: 'c', 4: 'd'})
        ```
        """
        ...
    
    @overload
    def get(self, key: K, /) -> V:
        """Get a value for a given key.

        If the key is not present in the `HashMap`,
        raises HashMap Error.
        """
        ...
    
    @overload
    def get(self, key: K, *, default: Union[V, Any, None] = None) -> Union[V, Any, None]:
        """Get a value for a given key.
        
        Returns `default` value if key is not
        present in the `HashMap`
        """
        ...
    
    def clear(self) -> None:
        """`clear all key-value pairs.`"""
        ...
    
    @overload
    def update_using(self, other: 'HashMap[K, V]') -> None:
        """Update the current `HashMap` using another `HashMap`.
        
        - Keys will be added if not present in the current `HashMap`.
        - Values will be updated if key is present in the current `HashMap`.
        """
        ...

    @overload
    def update_using(self, other: Union[Mapping[K, V], Dict[K, V]]) -> None:
        """Update the current `HashMap` using some Dict or Mapping.
        
        - Keys will be added if not present in the current `HashMap`.
        - Values will be updated if key is present in the current `HashMap`.
        """
        ...
    
    @overload
    def update_using(self, other: Iterable[Tuple[K, V]]) -> None:
        """Update the current `HashMap` using an Iterable whose
        elements are Tuple of length 2:  (key, value).
        
        - Keys will be added if not present in the current `HashMap`.
        - Values will be updated if key is present in the current `HashMap`.
        """
        ...
    
    def flatten(self) -> bytes:
        """Flatten the `HashMap` to bytes for sending over
        socket server or to serve some other purpose.
        
        Uses `pickle.dumps` for flattening.

        For getting the data back, use `HashMap(flattened_hashmap)`.
        
        Example:
        ```python
        >>> from modstore import HashMap
        >>> h = HashMap({1: 2, 2: 3, 3: 4, 4:5})
        >>> new = HashMap(h.flatten())
        >>> new
        HashMap({1: 2, 2: 3, 3: 4, 4: 5})
        ```
        """
        ...
    
    def setdefault(self, key: K, default: Callable[[], V], /) -> None:
        """Set a default value for a key.
        
        The Key must not be present in the `HashMap`, else `HashMapError`
        will be raised.
        """
        ...

class _hasher:
    """Hasher class for hashing objects."""
    def __init__(self, hashf: Literal['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'] = 'md5') -> None: ...
    def hash(self, object: object) -> str: ...

class AutoHashMap(Generic[K, E]):
    """`AutoHashMap Class`
    
    - Supports custom hash functions.
    - Keys are hashes of the values.
    - Has pre-defined hash function: `['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']`
    - Handles Collision using Grouping. The most recently added data
      will be at the end of the group (list).

    `AutoHashMap` uses hash of the values as keys, providing a consistent
    Hash Table. Custom Hash Functions are supported along with predefined
    hash functions.

    `Keys` are auto-generated and the user cannot manually change keys for a value.
    However, the `hash_function` can be replaced.

    `Working:`
    
    Maintains a `Hash Table` like object, where the keys are auto-generated
    using a given hash function. The values to be inserted are passed to
    the hash function to get the key. If the key already exists (collision),
    the values with the same hash are grouped together in a list (where the
    most recently added value will be at the end of the list). This grouping
    is done better handling and availability of data.
    """
    
    SUPPORTED_HASH: basicList[str]
    _inner: hashmap_internal_object[K, Union[E, basicList[E]]]

    @overload
    def __init__(self) -> None:
        """Create an empty `AutoHashMap`.
        
        The Hash Function needs to be set explicitly using
        `set_hashf` method.
        """
        ...
    
    @overload
    def __init__(self, *, create_from: Iterable[E]) -> None:
        """Create an `AutoHashMap` with a given iterable of values.
        
        The values will be added using `md5` hash function. if multiple
        values are found to have the same hash (highly unlikely), they will
        be grouped together in a list for that hash digest.

        Example:
        ```python
        >>> from modstore import AutoHashMap
        >>> ahm = AutoHashMap(create_from=[1, 'a', 4, 'd'])
        ```
        """
        ...
    
    @overload
    def __init__(self, *, create_from: Iterable[E], hash_function: Callable[[E], K]) -> None:
        """Create an `AutoHashMap` with a given iterable of values
        and given hash function.
        
        The hash function should take the values from iterable and
        return some unique object as key (for that value).

        If multiple values generate the same key, they will be grouped
        together in a list.

        Example:
        ```python
        >>> from modstore import AutoHashMap
        >>> ahm = AutoHashMap(
        ...         create_from = [1, 2, 3, 4],
        ...         hash_function = lambda x: 2*x
        ... )
        ...
        >>> ahm
        AutoHashMap({2: 1, 4: 2, 6: 3, 8: 4})
        ```
        """
        ...
    
    @overload
    def __init__(self, *, create_from: Iterable[E], hash_function: Literal['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']) -> None:
        """Create an `AutoHashMap` with a given iterable of values
        and pre-defined hash function.
        
        Choose any `hash_function` from: `['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']`
        and specify in the `hash_function` parameter.

        if multiple values are found to have the same hash (highly unlikely),
        they will be grouped together in a list for that hash digest.

        Example:
        ```python
        >>> from modstore import AutoHashMap
        >>> ahm = AutoHashMap(
        ...         create_from = [1, 2, 3, 4, 'a', 'b'],
        ...         hash_function = 'sha256'
        ... )
        ```
        """
        ...
    
    # internal methods
    def _adder(self, key: K, value: E) -> None: ...
    def _update_according_to_function(self, old_function: Union[_hasher, Callable[[E], K], None], new_function: Union[_hasher, Callable[[E], K]]) -> None: ...
    def _get_flattened_values(self) -> hashmap_values[E]: ...

    def __iter__(self) -> Iterator[K]: ...
    def __contains__(self, item: E) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

    # methods
    def insert(self, value: E) -> None:
        """Insert a value into the Hash Map.
        
        The hash function must be set at this point.
        If not, use `set_hashf` method to avoid raising
        `HashMapError`.
        """
        ...
    
    @overload
    def set_hashf(self, function: Callable[[E], K]) -> None:
        """Set a custom hash function.
        
        If this method is called while a hash function is set and some
        data is there, the keys will be replaced with new hash keys
        automatically.
        """
        ...
    
    @overload
    def set_hashf(self, function: Literal['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']) -> None:
        """Set a pre-defined hash function.
        
        If this method is called while a hash function is set and some
        data is there, the keys will be replaced with new hash keys
        automatically.
        """
        ...
    
    def get_hashf(self) -> Union[Callable[[E], K], None]:
        """Get The Hash Function if set."""
        ...
    
    @overload
    def iter(self) -> hashmap_items[K, Union[E, basicList[E]]]:
        """returns an iterator over the the keys and values."""
        ...
    
    @overload
    def iter(self, step: int = 1, /) -> hashmap_items[K, Union[E, basicList[E]]]:
        """returns an iterator over the keys and values.
        
        `step` defines the increment value of the iterator
        similar to `range()` function.
        """
        ...
    
    @overload
    def iterkeys(self) -> hashmap_keys[K]:
        """returns an iterator over the keys."""
        ...
    
    @overload
    def iterkeys(self, step: int = 1, /) -> hashmap_keys[K]:
        """returns an iterator over the keys.
        
        `step` defines the increment value of the iterator
        similar to `range()` function.
        """
        ...
    
    @overload
    def itervalues(self) -> hashmap_values[Union[E, basicList[E]]]:
        """returns an iterator over the values."""
        ...
    
    @overload
    def itervalues(self, step: int = 1, /) -> hashmap_values[Union[E, basicList[E]]]:
        """returns an iterator over the values.
        
        `step` defines the increment value of the iterator
        similar to `range()` function.
        """
        ...
    
    def pop(self, value: E) -> Union[K, None]:
        """If the value exists in the HashMap,
        removes it and returns the key value.
        
        Else returns None.

        Any Grouped value, if reduced to one element after pop,
        will be ungrouped.
        """
        ...
    
    def getitems(self) -> basicList[Tuple[K, Union[E, basicList[E]]]]:
        """Get a list of all items.
        
        Return Format: `List[Tuple[Key, Element]]`
        """
        ...
    
    def getkeys(self) -> basicList[K]:
        """Get a list of keys."""
        ...
    
    def getvalues(self, *, flatten: bool = False) -> basicList[Union[E, basicList[E]]]:
        """Get a list of values.
        
        If not flattened, might return list of list. [`List[E | List[E]]`]

        If flattened, will return `List[E]`.
        """
        ...
    