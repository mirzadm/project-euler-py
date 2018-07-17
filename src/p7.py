"""nth prime number."""

from math import sqrt


def is_prime(m, primes):
    """Checks primality of m given "enough" prime numbers.

    Args:
        m: Number to check.
        primes: A sorted list inlcuding all prime numbers <= sqrt(m)
    """
    m_sqrt = int(sqrt(m))
    is_prime = True
    i = 0
    while i < len(primes) and primes[i] <= m_sqrt and is_prime:
        if m % primes[i] == 0:
            is_prime = False
        i += 1
    return is_prime


def nth_prime_number(n):
    """Returns nth prime number.
    
    Uses `is_prime`.
    Args:
        n: Integer >= 1.
    Raises:
        IndexError: If n < 1.
    """
    if n < 1:
        raise IndexError('Input argument must be >= 1.')
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate, primes):
            primes.append(candidate)
        candidate += 1

    return primes[-1]
