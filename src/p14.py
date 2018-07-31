"""Project Euler: Problem 14."""


def calculate_sequence_length(n, length_dict):
    """Calculates the sequence length for `n`.

    The sequence: 
        n --> n/2   if n even
        n --> 3n+1  if n odd
        ends        if n is 1

    Uses and updates `length_dict` dicitonary in the process.
    """
    if n < 1:
        raise ValueError('Invalid input argument.')

    if n not in length_dict:
        if n == 1:
            length_dict[n] = 1
        else:
            if n % 2 == 0:
                length_dict[n] = 1 + calculate_length(n // 2, length_dict)
            else:
                length_dict[n] = 1 + calculate_length(3 * n + 1, length_dict)

    return length_dict[n]
