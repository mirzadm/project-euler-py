"""Project Euler: Problem 12."""

from src.p5 import prime_factorization


def triangular_number_generator():
    """Creates a generator for triangular numbers.

    Triangular numbers:
    1, 3, 6, 10, 15, 21, 28, ...
    """
    current = 0
    sum = 0
    while True:
        current += 1
        sum += current
        yield sum 


def find_special_triangular_num(num_of_divisors_threshold):
    """Returns first triangular number given number of divisors condition.
    
    Finds first triangular number with number of divisors greater than
    `num_of_divisors_threshold`. 

    Uses prime factorization method.

    Args:
        `num_of_divisors_threshold`: Positive integer.
    """
    for i in triangular_number_generator():
        primes = prime_factorization(i)
        num_of_divisors = 1
        for factor, power in primes.items():
            num_of_divisors *= (power + 1)

        if num_of_divisors > num_of_divisors_threshold:
            return i
