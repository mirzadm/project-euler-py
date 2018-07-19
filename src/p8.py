"""Project Euler: Problem 8."""


def find_adj_digits_with_max_product(num_str, num_of_adj_digits):
    """Finds adjacent digits in a given number producing the greatest product.
    
    Finds in `num_str` a sequence of adjacent digits of size
    `num_of_adj_digits` that yields the greatest product.
    
    Example:
        num_str = '123'
        num_of_adj_digits = 2
        The sequence '23' gives the greatest product which is 6.

    Args:
        num_str: A string formatted unsigned integer.
        num_of_adj_digits: Postive interger.
    Returns:
        A tuple of max product value and starting index of the max product
        sequence.
    Raises:
        ValueError: If num_of_adj_digits is bigger than num_str.
    """
    digits_array = [int(ch) for ch in num_str] # Throws exception if malformed
    n = len(digits_array)
    
    if num_of_adj_digits > n or num_of_adj_digits <= 0:
        raise ValueError('Invalid input argument.')
    i = 0
    adj_length = 0
    product = 1
    max_product = 0
    max_index = 0
    while i < n:
        while i < n and adj_length < num_of_adj_digits and digits_array[i] != 0:
            product *= digits_array[i]
            i += 1
            adj_length += 1
        if adj_length == num_of_adj_digits:
            if product > max_product:
                max_product = product
                max_index = i - num_of_adj_digits
            # Update product for the next round
            product //= digits_array[i - num_of_adj_digits]
            adj_length -= 1
        elif i == n:
            break
        # digits_array[i] == 0
        else:
            adj_length = 0
            i += 1
            product = 1

    return (max_product, max_index)
 