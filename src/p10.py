"""Project Euler: Problem 10."""

from src.p7 import is_prime


def sum_of_primes(max_value):
    """Finds sum of all prime number < `max_value`."""
    primes = []
    total = 0
    candidate = 2
    while candidate < max_value:
        if is_prime(candidate, primes):
            primes.append(candidate)
            total += candidate
        candidate += 1

    return total
