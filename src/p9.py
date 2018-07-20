"""Project Euler: Problem 9."""


def special_pythagorean_triplet(triplet_sum):
    for a in range(1, triplet_sum // 2):
        for b in range(a + 1, triplet_sum - a):
            c = triplet_sum - a - b
            if c > 0:
                if c < a or (c > a and c < b):
                    if c * c + a * a == b * b:
                        return (c, a, b)
                if c > b:
                    if a * a + b * b == c * c:
                        return (a, b, c)
    return None