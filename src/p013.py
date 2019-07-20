"""Project Euler: Problem 13."""


def sum_str_nums(str_num1, str_num2, step=10):
    """Sums up two long string formatted integers.
    
    Adds up two string formatted integers iteratively, `step` digits at a time.

    Args:
        `str_num1`, `str_num2`: String formatted unsigned integers.
        `step`: Positive integer.
    Return:
        String formatted sum.
    """
    if step <= 0:
        raise ValueError("`step` must be a positive integers.")
    right1 = len(str_num1)
    right2 = len(str_num2)
    carry = 0
    result = ""
    step_power = 10 ** step
    while right1 > 0 or right2 > 0:
        if right1 >= step:
            op1 = int(str_num1[right1 - step: right1])
            right1 -= step
        elif right1 > 0:
            op1 = int(str_num1[0: right1])
            right1 = 0
        else:
            op1 = 0

        if right2 >= step:
            op2 = int(str_num2[right2 - step: right2])
            right2 -= step
        elif right2 > 0:
            op2 = int(str_num2[0: right2])
            right2 = 0
        else:
            op2 = 0

        next_sum = op1 + op2 + carry
        carry = next_sum // step_power
        next_step_sum = next_sum % step_power
        if right1 > 0 or right2 > 0:
            result = str(next_step_sum).zfill(step) + result
        else:
            result = str(next_sum) + result
    return result


def add_list_str_nums(str_nums):
    """A wrapper to solve the main problem with."""
    result = str_nums[0]
    for str_num in str_nums[1: ]:
        result = sum_str_nums(result, str_num)
    return result
