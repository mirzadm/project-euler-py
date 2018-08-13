"""Project Euler: Problem 8."""


def find_current_len_with_max_product(str_num, adj_len):
    """Finds adjacent digits in a number that produce the greatest product.
    
    Finds in `str_num` a sequence of adjacent digits of size
    `adj_len` that yields the greatest product.
    
    Example:
        str_num = '4567'
        adj_len = 2
        The sequence '67' gives the greatest product which is 42.

    Args:
        str_num: A string-formatted unsigned integer.
        adj_len: Postive interger.
    Returns:
        A tuple of max product value and starting index of the max product
        sequence.
    Raises:
        ValueError: If adj_len is bigger than str_num.
    """
    digits_array = [int(ch) for ch in str_num] # Throws exception if malformed
    n = len(digits_array)
    
    if adj_len > n or adj_len <= 0:
        raise ValueError('Invalid input argument.')

    i = 0
    current_len = 0
    current_prod = 1
    max_product = 0
    max_index = 0
    while i < n:
        while i < n and current_len < adj_len and digits_array[i] != 0:
            current_prod *= digits_array[i]
            i += 1
            current_len += 1
        if current_len == adj_len:
            if current_prod > max_product:
                max_product = current_prod
                max_index = i - adj_len
            # Update current_prod for the next round
            current_prod //= digits_array[i - adj_len]
            current_len -= 1
        elif i < n and digits_array[i] == 0:
            current_len = 0
            i += 1
            current_prod = 1

    return (max_product, max_index)
 