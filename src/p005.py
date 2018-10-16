"""Smallest number divisible to all number from 1 to n."""


def prime_factorization(n):
    """Returns prime factors as a dictionary.

    It is not an efficient implementation but gets the job done.
    """
    prime_factors = {}
    i = 2
    while n > 1:
        k = 0
        while n % i == 0 and n > 1:
            n = n // i
            k += 1
        if k > 0:
            prime_factors[i] = k
        i += 1
    return prime_factors


def smallest_divisible_number(n):
    """Finds the smallest number divisble to all number from 1 to n."""
    prime_factors = {}
    for i in range(2, n+1):
        new_factors = prime_factorization(i)
        for factor, power in new_factors.items():
            if factor in prime_factors:
                if prime_factors[factor] < power:
                    prime_factors[factor] = power
            else:
                prime_factors[factor] = power

    smallest_divisible = 1
    for factor, power in prime_factors.items():
        smallest_divisible *= factor ** power

    return smallest_divisible
