"""Project Euler: Problem 3."""


def largest_prime_factor(n):
    """Finds largest prime factor of `n`.
    
    Args:
        n: Integer greater than 1.
    Raises:
        ValueError: For `n` <= 1.
    """
    if n <= 1:
        raise ValueError('Invalid input argument.')

    i = 2
    while n > 1:
        if n % i == 0:
            last_prime_factor = i
            while n % i == 0:
                n = n // i
        i += 1

    return last_prime_factor
