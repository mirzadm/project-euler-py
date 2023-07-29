"""Project Euler: Problem 20

Uses an array to store digits, as if int had limited bits.
"""

from typing import List


def multiply_digit_array_by_single_digit(
    multiplicand_array: List[int], multiplier: int
) -> List[int]:
    product_array = []
    rest = 0
    for digit in multiplicand_array:
        product = digit * multiplier + rest
        ones = product % 10
        rest = product // 10
        product_array.append(ones)
    while rest > 0:
        product_array.append(rest % 10)
        rest = rest // 10
    return product_array


def calculate_factorial_digits(n: int) -> List[int]:
    factorial_digits = [1]
    for i in range(2, n + 1):
        factorial_digits = multiply_digit_array_by_single_digit(factorial_digits, i)
    return factorial_digits


if __name__ == "__main__":
    print(sum(calculate_factorial_digits(100)))
