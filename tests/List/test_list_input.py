from modstore.python import List
from unittest.mock import patch

import pytest

@pytest.fixture
def setup():
    custom_list = List()

    return custom_list

def test_input(setup):
    custom = setup

    with patch('builtins.input', side_effect=["1 2 3 4 5"]):
        custom.fillByInput(' ')

        assert type(custom) == List
        assert len(custom) == 5
        assert type(custom[0]) == int

def test_creating_from_string():
    """`Test List Creation from string ability.`"""
    list_ = List(['a', 'b', 'c', 'd'])
    list_.fillByString("efgh", None, list)

    assert list_ == List(['a', 'b', 'c', 'd', ['e', 'f', 'g', 'h']])
    
    list_ = list_.flatten
    assert list_ == List(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])