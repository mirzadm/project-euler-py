"""Project Euler: Problem 10."""

from math import sqrt


def sum_of_primes(upper_limit):
    """Finds sum of all prime numbers < `upper_limit`.
    
    Uses the method known as sieve of Eratosthenes.
    
    Args:
        `upper_limit`: Positive integer. 
    Returns:
        Sum of all prime numbers less than `upper_limit`. 
        0 if `upper_limit` less than 3.
    Raises:
        ValueError: If `upper_limit` less than 1.
    """
    if upper_limit < 1:
        raise ValueError('Input argument must be greater than or equal to 1.')
    
    # Default to prime
    # Numbers 0 and 1 are also included here but just to simplify
    # index-number relation. They are not actually used.
    is_prime_array = [True] * upper_limit  

    upper_limit_sqrt = int(sqrt(upper_limit))
    
    for n in range(2, upper_limit_sqrt + 1):
        if is_prime_array[n]:
            for i in range(2 * n, upper_limit, n):
                is_prime_array[i] = False
    
    total = 0
    for n in range(2, upper_limit):
        if is_prime_array[n]:
            total += n

    return total
