"""Project Euler: Problem 7."""


def is_prime(m, primes):
    """Checks primality of `m` with respect to given `primes`.

    For the function to work properly, `primes` must at least have all the
    prime numbers up to square root of `m`.
    
    Args:
        `m`: Integer value greater than 1.
        `primes`: A list of prime numbers. 
    Raises:
        ValueError: For `m` less than or equal to 1.
    """
    if m <= 1:
        raise ValueError('Invalid input argument.')

    sq_root = int(m ** 0.5)
    i = 0
    while i < len(primes) and primes[i] <= sq_root:
        if m % primes[i] == 0:
            return False
        i += 1
    return True


def nth_prime_number(n):
    """Returns nth prime number.
    
    Uses `is_prime`.

    Args:
        `n`: Positive integer.
    Raises:
        ValueError: For `n` less than 1.
    """
    if n < 1:
        raise IndexError('Invalid input argument.')

    primes = []
    candidate = 2
    num_of_primes = 0
    while num_of_primes != n:
        if is_prime(candidate, primes):
            primes.append(candidate)
            num_of_primes += 1
        candidate += 1

    return primes[-1]
