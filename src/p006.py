"""Calculates: (1+2+...+n)**2  -  (1**2 + 2**2 + ... + n**2).

Only calculates the remaining terms after the subtraction.
2*i*j where i != j.
"""

def square_of_sum_minus_sum_of_squares(n):
    if n < 1:
        raise ValueError('Input argument must be >= 1.')
    total = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i != j:
                total += 2 * i * j
    return total
