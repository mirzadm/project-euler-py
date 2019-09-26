"""Project Euler: Problem 18"""


def max_length_to_every_bottom_element(nums):
    """Finds max length from top to bottom row (all elements) in pyramid.

    Example:
        Input: [1, 2, 3, 4, 5, 6] represents the following pyramid:
                1
               2 3
              4 5 6
        For which max length to last row [4, 5, 6] is [7, 9, 10]

    Args:
        `nums`: List of integers.
    Returns:
        List of max length to every element in the last row of the pyramind.
    """
    if not nums:
        return []

    base = 1
    current_row_maxes = [nums[0]]
    while base < len(nums):
        next_row_maxes = []
        for offset in range(len(current_row_maxes)):
            if offset == 0:
                adj_max = current_row_maxes[offset]
            else:
                adj_max = max(current_row_maxes[offset - 1: offset + 1])
            next_max = nums[base + offset] + adj_max
            next_row_maxes.append(next_max)
        next_max = nums[base + offset + 1] + current_row_maxes[offset]
        next_row_maxes.append(next_max)
        base += len(next_row_maxes)
        current_row_maxes = next_row_maxes
    return current_row_maxes
