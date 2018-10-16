"""Project Euler: Problem 10."""


def sum_of_primes(upper_limit):
    """Finds sum of all prime numbers < `upper_limit`.
    
    Uses the method known as sieve of Eratosthenes.
    
    Args:
        `upper_limit`: Positive integer. 
    Returns:
        Sum of all prime numbers less than `upper_limit`. 
    Raises:
        ValueError: If `upper_limit` less than 1.
    """
    if upper_limit < 1:
        raise ValueError('Input argument must be greater than or equal to 1.')
    
    primes = [True] * upper_limit

    upper_limit_sqrt = int(upper_limit ** 0.5)
    
    primes_sum = 0
    for n in range(2, upper_limit_sqrt+1):
        if primes[n]:
            primes_sum += n
            for i in range(2*n, upper_limit, n):
                primes[i] = False
    
    for n in range(upper_limit_sqrt+1, upper_limit):
        if primes[n]:
            primes_sum += n

    return primes_sum
