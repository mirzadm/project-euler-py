"""Project Euler: Problem 14."""


# def find_longest_sequence(upper_limit):
#     """Finds the number in 1 to `upper_limit` generating the longest sequence.

#     The sequence: 
#         n --> n/2   if n even
#         n --> 3n+1  if n odd
#         ends        if n is 1
#     """

#     visited = {}
#     longest = 0
#     i = upper_limit
#     while i > 1:
#         if i in visited:
#             i -= 1
#             continue
#         else:

#             if 


def sequence_length(n):
    k = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        k += 1
    return k

def find_max(m):
    max_seq = 0
    max_num = None
    for i in range(m, 1, -1):
        k = sequence_length(i) 
        if k > max_seq:
            max_seq = k
            max_num = i
    
    return (max_num, max_seq)