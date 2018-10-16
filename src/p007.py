"""Project Euler: Problem 7."""


def nth_prime_number(n):
    """Returns nth prime number.

    Args:
        `n`: Positive integer.
    Raises:
        IndexError: For `n` less than 1.
    """
    if n < 1:
        raise IndexError('Invalid input argument.')

    primes = []
    candidate = 2
    num_of_primes = 0
    while num_of_primes != n:
        i = 0
        is_prime = True
        while i < len(primes) and primes[i] <= int(candidate ** 0.5):
            if candidate % primes[i] == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            primes.append(candidate)
            num_of_primes += 1

        candidate += 1

    return primes[-1]
