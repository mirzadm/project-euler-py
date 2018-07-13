"""The largest prime factor of n."""

from math import sqrt


def is_prime(m, primes):
    """Checks primality of m given "enough" prime numbers.

    Args:
        m: Number to check.
        primes: A list inlcuding at least all prime numbers <= sqrt(m)
    """
    m_sqrt = int(sqrt(m))
    is_prime = True
    i = 0
    while i < len(primes) and primes[i] <= m_sqrt and is_prime:
        if m % primes[i] == 0:
            is_prime = False
        i += 1
    return is_prime


def prime_numbers_up_to(x):
    """Returns list of prime numbers <= x.
    
    Uses `is_prime`.
    """
    primes = []
    for i in range(2, x+1):
        if is_prime(i, primes):
            primes.append(i)
    return primes


def largest_prime_factor(n):
    """Find the largres prime factor of n."""
    if n < 2:
        return None
    # Find all prime number <= sqrt(n)
    primes = prime_numbers_up_to(int(sqrt(n)))
    # Filter prime factors of n
    prime_factors_subset = []
    for p in primes:
        if n % p == 0:
            prime_factors_subset.append(p)
    # Check primality of n
    if prime_factors_subset == []:
        return n
    # Find maximum prime factor
    i = 0
    while i < len(prime_factors_subset) and n > 1:
        while n % prime_factors_subset[i] == 0:
            n = n // prime_factors_subset[i]
        i += 1
    if n > 1:
        return n
    else:
        return prime_factors_subset[-1]
