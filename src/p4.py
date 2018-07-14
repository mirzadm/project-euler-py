"""Largest palindrome number that is a product of 2 three-digit numbers."""


def convert_num_to_digits_list(num):
    """Converts a non-negative int to its list of digits in reverse order."""
    if num < 0:
        raise ValueError('Input argument has to be non-negative.')
    if num == 0:
        return [0]
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    return digits


def is_palindrome(num):
    """Checks whether number is a palindrome."""
    pos_num = abs(num)
    digits = convert_num_to_digits_list(pos_num)
    n = len(digits)
    mid = n // 2
    for i in range(mid):
        if digits[i] != digits[n-i-1]:
            return False
    return True


def find_largest_palindrome():
    """Finds largest palindrome in products of 2 three-digit numbers."""
    max_palindrome = 0
    for n in range(100, 1000):
        for m in range(n, 1000):
            product = m * n
            if is_palindrome(product):
                if product > max_palindrome:
                    max_palindrome = product
    if max_palindrome == 0:
        return None
    else:
        return max_palindrome
