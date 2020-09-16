import pytest
from python_algo_solutions import add_binary

def test_should_add_with_no_leading_zeros():

    assert add_binary.binary_sum("101", "1") == "110"
    assert add_binary.binary_sum("100", "1") == "101"
    assert add_binary.binary_sum("11", "1") == "100"
    assert add_binary.binary_sum("1", "0") == "1"
    assert add_binary.binary_sum("101101", "11001") == "1000110"
    assert add_binary.binary_sum("1001", "110110") == "111111"

def test_should_return_an_empty_string():

    assert add_binary.binary_sum("", "") == ""

def test_should_return_the_non_empty_bin():

    assert add_binary.binary_sum("100", "") == "100"
    assert add_binary.binary_sum("", "10001") == "10001"

