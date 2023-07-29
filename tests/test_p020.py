"""Unit tests for problem 20"""

from src.p020 import calculate_factorial_digits
def test_calculate_factorial_digits():
    assert calculate_factorial_digits(1) == [1]
    assert calculate_factorial_digits(2) == [2]
    assert calculate_factorial_digits(3) == [6]
    assert calculate_factorial_digits(4) == [4, 2]
    assert calculate_factorial_digits(5) == [0, 2, 1]
    assert calculate_factorial_digits(6) == [0, 2, 7]
