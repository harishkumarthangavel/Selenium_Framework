from scripts.factorial_example import factorial_func
import pytest
import math

def test_factorial_functionality():
    print("Testing factorial functionality")
    assert factorial_func(0) == 1
    assert factorial_func(5) == 120

def test_factorial_std_lib():
    print("Testing factorial against stdlib")
    for i in range(6):
        assert factorial_func(i) == math.factorial(i)

def test_negative_input():
    print("Testing negative input")
    with pytest.raises(AssertionError):
        factorial_func(-3)