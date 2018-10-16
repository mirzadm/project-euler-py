"""Sum of numbers < n that are multiples 3 or 5."""


def sum_of_multiples_3_or_5(n):
    sum = 0
    for x in range(3, n):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum
