"""Project Euler: Problem 14."""


def update_sequence_length_map(n, num_to_seq_len_map={}):
    """Updates map with required/missing items for `n`s sequence.

    Next element in `n`s sequence:
        n --> n/2   if n even
        n --> 3n+1  if n odd
        1 --> 1

    Example:
        Sequence starting at 10:
            10, 5, 16, 8, 4, 2, 1
        Corresponding `num_to_seq_len_map`:
            {10: 7, 5: 6, 16: 5, 8: 4, 4: 3, 2: 2, 1: 1}
    
    Args:
        `n`: Positive integer.
        `num_to_seq_len_map`: Map of numbers to their sequence lengths.
    Returns:
        Updated sequence map
    """
    if n < 1:
        raise ValueError('Invalid input argument.')

    if n not in num_to_seq_len_map:
        if n == 1:
            num_to_seq_len_map[n] = 1
        elif n % 2 == 0:
            num_to_seq_len_map = update_sequence_length_map(
                n // 2, num_to_seq_len_map
            )
            num_to_seq_len_map[n] = 1 + num_to_seq_len_map[n // 2]
        else:
            num_to_seq_len_map = update_sequence_length_map(
                3 * n + 1, num_to_seq_len_map
            )
            num_to_seq_len_map[n] = 1 + num_to_seq_len_map[3 * n + 1]
    return num_to_seq_len_map