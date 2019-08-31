"""Project Euler: Problem 16"""


def calc_big_power_of_two(p):
    """Calculates 2 to the `p`.

    Arg:
        `p`: Nonegative integer.
    Returns:
        List of digits of 2 to `p`. Least important digit first.
    Raises:
        ValueError: negative `p`.
    """
    if p < 0:
        raise ValueError("Value of power should be non-negative.")
    result_digits = [1]
    for _ in range(p):
        carry = 0
        for i in range(len(result_digits)):
            next_sum = carry + result_digits[i] * 2
            carry = next_sum // 10
            result_digits[i] = next_sum % 10
        if carry:
            result_digits.append(carry)
    return result_digits
