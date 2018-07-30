"""Project Euler: Problem 13."""


def string_number_to_list(number_string, digit_width):
    """Converts a string-formatted number to a list of its sub-digits.

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


def add_up_string_numbers(string_numbers, digit_width):
    """Adds a list of string numbers.

    The sum is calculated `digit_width` digits at a time.

    Args:
        `string_numbers`: A list of string-formatted unsigned integers.
        `digit_width`: Positive integer.
    Returns:
        A string representation of sum value.
    Raises:
        ValueError: For `digit_width` less than 1.
    """
    if digit_width < 1:
        raise ValueError('Invalid input argument value.')

    sum_array = []
    for string_num in string_numbers:
        num_array = string_number_to_list(string_num, digit_width)
        sum_array =  add_int_lists_with_carry(sum_array, num_array,
                                              digit_width)
    sum_string = ''
    if len(sum_array) > 0:
        sum_string = str(sum_array[0])
        sum_string += ''.join(str(sum_array[i]).zfill(digit_width) for i in
                              range(1, len(sum_array)))
    return sum_string
