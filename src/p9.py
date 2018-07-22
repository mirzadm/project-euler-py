"""Project Euler: Problem 9."""

from math import ceil


def special_pythagorean_triple(triple_sum):
    """Finds a special Pythogorean triple.
    
    Finds a triple that satisfies the following conditions:
        a < b < c
        a + b + c = triple_sum
        a**2 + b**2 = c**2

    Assume triple_sum is 1000.
    For every pair of (a, b) we can calculate: c = 1000 - (a + b).    
    One method is to look at all combinations of a and b such that a < b. We
    could then calculate c and if c > b, we would check if (a, b, c) forms a
    Pythagorean triple.

    A more efficient method would look at a subset of all (a, b) combinations.
    Given a < b, the smallest value for b would be: a + 1.
    We have the following inequalities: 
        b < c => a + 1 < 1000 - (a + (a + 1)) => 3a < 1000 - 2 =>
        a < (1000 - 2) / 3
    Also:
        b < c => b < 1000 - (a + b) => 2b < 1000 - a => b < (1000 - a) / 2
    
    The time complexity is stillw quadratic but the second method has about
    0.1 of iterations compared to the first method. 
    
    Args:
        triple_sum: A postivie integer resprenting sum value of the triple.
    Returns:
        A tuple of a triple is found. None otherwise.
    """
    permutations = 0
    for a in range(1, int(ceil((triple_sum - 2) / 3))):
        for b in range(a + 1, int(ceil((triple_sum - a) / 2))):
            c = triple_sum - (a + b)
            if a * a + b * b == c * c:
                return (a, b, c)
    return None
