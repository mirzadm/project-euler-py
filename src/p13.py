"""Project Euler: Problem 13."""


def add_num_str(num_str1, num_str2, digit_step):
    """Returns sum of two string-formatted numbers as a string.
    
    Calculates the sum `digit_step` digits at a time.
    For instance, with `digit_step` of 1 calculation is done 1 digit at a
    time.

    Args:
        num_str1, num_str2: String formated unsigned integers.
    Returns:
        Sum value as a string.
    """
    if digit_step < 1:
        raise ValueError('Invalid input argument.')

    n1 = len(num_str1)
    n2 = len(num_str2)
    
    result = ''
    power_of_10 = 10 ** digit_step
    carry = 0    
    i1 = n1
    i2 = n2 
    while i1 > 0 or i2 > 0:
        if i1 >= digit_step:
            first_operand = int(num_str1[i1 - digit_step : i1])
            i1 -= digit_step
        elif i1 > 0:
            first_operand = int(num_str1[ : i1])
            i1 = 0
        else:
            first_operand = 0

        if i2 >= digit_step:
            second_operand = int(num_str2[i2 - digit_step : i2])
            i2 -= digit_step
        elif i2 > 0:
            second_operand = int(num_str2[:i2])
            i2 = 0
        else:
            second_operand = 0


        next_sum =  first_operand + second_operand + carry
        carry = next_sum // power_of_10
        if carry == 0 and i1 == 0 and i2 == 0:
            new_str_sum = str(next_sum % power_of_10)
        else:
            new_str_sum = str(next_sum % power_of_10).zfill(digit_step)
        result = new_str_sum + result

    if carry > 0:
        result = str(carry) + result

    return result


