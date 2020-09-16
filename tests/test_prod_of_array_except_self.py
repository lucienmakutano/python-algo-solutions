import pytest
from python_algo_solutions import product_of_array_except_self as poaes

def test_should_return_prod_of_array_el_except_self():

    assert poaes.solution([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert poaes.solution([3, 2, 1]) == [2, 3, 6]
    assert poaes.solution([1, 2, 3, 4]) == [24, 12, 8, 6]

