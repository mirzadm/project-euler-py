"""Sum of even numbers in Fibonacci series."""


def sum_of_even_fibo_nums(n):
    """Returns sum of even numbers <= n in Fibonacci series.
    
    Fibonacci series: 1, 2, 3, 5, 8, 13, ...
    """
    current = 1
    previous = 1
    total = 0
    while current <= n:
        if current % 2 == 0:
            total += current
        current, previous = current + previous, current

    return total
