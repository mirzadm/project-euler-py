"""Project Euler: Problem 14."""


def calculate_sequence_length(n, length_dict):
    """Calculates the sequence length for `n`.

    The sequence: 
        n --> n/2   if n even
        n --> 3n+1  if n odd
        ends        if n is 1
    
    Example:
        Sequence starting at 10:
            10, 5, 16, 8, 4, 2, 1
        Corresponding dicitonary:
            {10: 7, 5: 6, 16: 5, 8: 4, 4: 3, 2: 2, 1: 1}

    Reads and mutates `length_dict` dicitonary.
    
    Args:
        `n`: Positive integer.
        `length_dict`: A dictionary of previously calculated sequence terms
                       and their corresponding lengths.
    Returns:
            Length of the sequence starting at `n`
    """
    if n < 1:
        raise ValueError('Invalid input argument.')

    if n not in length_dict:
        if n == 1:
            length_dict[n] = 1
        else:
            if n % 2 == 0:
                length_dict[n] = 1 + calculate_sequence_length(n // 2,
                                                               length_dict)
            else:
                length_dict[n] = 1 + calculate_sequence_length(3 * n + 1,
                                                               length_dict)

    return length_dict[n]
