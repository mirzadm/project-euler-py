"""Project Euler: Problem 13."""


def number_string_to_list(number_string, digit_width):
    """Converts a string-formatted number to a list of partial integers.

    Starting from right, slices the string to `digit_width` size pieces.
    Then converts each slice to an integer and stores it in a list.
    Example:
        `number_string` : '12345'
        `digit_width` : 2
         returns: [1, 23, 45]

    Args:
        `number_string`: A string-formatted unsigned integer.
        `digit_width`: Positive integer.
    Returns:
        A list of unsigned integers.
    Raises:
        ValueError: For `digit_width` less than 1.
    """
    if digit_width < 1:
        raise ValueError('Invalid input argument value.')

    result = []
    i = len(number_string)
    while i > digit_width:
        next_slice = number_string[i - digit_width:i]
        result.insert(0, int(next_slice))
        i -= digit_width
    if i > 0:
        next_slice = number_string[:i]
        result.insert(0, int(next_slice))

    return result


def add_int_lists_with_carry(first_int_list, second_int_list, digit_width):
    """Adds two lists of integers from right to left with carry.

    Assumes each integer has no more than `digit_width` digits.
    Example:
        `digit_width`:                   2
        `first_int_list`:   [1,  0, 99] --> 10099
        `second_int_list`:     [99,  1] -->  9901  
        returns:            [2,  0,  0] --> 20000

    Args:
        `first_int_list`, `second_int_list`: Lists of unsigned integers with
            no more than `digit_width` digits.
        `digit_width`: Positive integer.
    Returns:
        A list of integers.
    Raises:
        ValueError: For `digit_width` less than 1.
    """
    if digit_width < 1:
        raise ValueError('Invalid input argument value.')
    # Identify longer and shorter number lists
    long_num, short_num = first_int_list, second_int_list
    if len(long_num) < len(short_num):
        long_num, short_num = short_num, long_num

    result = []
    short_index = len(short_num) - 1
    long_index = len(long_num) - 1
    power_of_10 = 10 ** digit_width
    carry = 0
    while short_index >=0:
        new_sum = long_num[long_index] + short_num[short_index] + carry
        carry = new_sum // power_of_10
        result.insert(0, new_sum % power_of_10)
        short_index -= 1
        long_index -= 1

    while long_index >= 0:
        new_sum = long_num[long_index] + carry
        carry = new_sum // power_of_10
        result.insert(0, new_sum % power_of_10)
        long_index -= 1

    if carry > 0:
        result.insert(0, carry)

    return result
