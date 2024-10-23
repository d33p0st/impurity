
from modstore.algorithms.searching import Search, SearchObject
from modstore.exceptions import IterableHasUnsupportedTypeValues

DATA_INT = [1, 2, 3, 4, 5]
DATA_STR = ['a', 'b', 'c', 'd', 'e']
searchObj_int = SearchObject(DATA_INT, 3)
searchObj_str = SearchObject(DATA_STR, 'c')

def test_linear():
    assert Search.linear(DATA_INT, 3) == 2
    assert searchObj_int.linear == 2
    assert Search.linear(DATA_STR, 'c') == 2
    assert searchObj_str.linear == 2

def test_sentinel_linear():
    assert Search.sentinel_linear(DATA_INT, 3) == 2
    assert searchObj_int.sentinel_linear == 2
    assert Search.sentinel_linear(DATA_STR, 'c') == 2
    assert searchObj_str.sentinel_linear == 2

def test_binary():
    assert Search.binary(DATA_INT, 3) == 2
    assert searchObj_int.binary == 2
    assert Search.binary(DATA_STR, 'c') == 2
    assert searchObj_str.binary == 2

def test_meta_binary():
    assert Search.meta_binary(DATA_INT, 3, 4, 1) == 2
    assert searchObj_int.meta_binary(4, 1) == 2
    assert Search.meta_binary(DATA_STR, 'c', 4, 1) == 2
    assert searchObj_str.meta_binary(4, 1) == 2

def test_ternary():
    assert Search.ternary(DATA_INT, 3, 4, 1) == 2
    assert searchObj_int.ternary(4, 1) == 2
    assert Search.ternary(DATA_STR, 'c', 4, 1) == 2 
    assert searchObj_str.ternary(4, 1) == 2

def test_jump():
    assert Search.jump(DATA_INT, 3) == 2
    assert searchObj_int.jump == 2
    assert Search.jump(DATA_STR, 'c') == 2
    assert searchObj_str.jump == 2

def test_interpolation():
    assert Search.interpolation(DATA_INT, 3) == 2
    assert searchObj_int.interpolation == 2

    try:
        somevalue = Search.interpolation(DATA_STR, 'c')
    except IterableHasUnsupportedTypeValues:
        assert True
    except Exception:
        assert False

def test_exponential():
    assert Search.exponential(DATA_INT, 3) == 2
    assert searchObj_int.exponential == 2
    assert Search.exponential(DATA_STR, 'c') == 2
    assert searchObj_str.exponential == 2

def test_fibo():
    assert Search.fibonacci(DATA_INT, 3) == 2
    assert searchObj_int.fibonacci == 2
    assert Search.fibonacci(DATA_STR, 'c') == 2
    assert searchObj_str.fibonacci == 2

def test_ubi_bin():
    assert Search.ubiquitous_binary(DATA_INT, 3) == 2
    assert searchObj_int.ubiquitous_binary == 2
    assert Search.ubiquitous_binary(DATA_STR, 'c') == 2
    assert searchObj_str.ubiquitous_binary == 2