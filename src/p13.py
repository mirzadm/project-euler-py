"""Project Euler: Problem 13."""


def add_num_str(first_num_string, second_num_string, digit_step):
    """Returns sum of two string-formatted numbers as a string.
    
    Calculates the sum `digit_step` digits at a time.
    For instance, with `digit_step` of 1 calculation is done 1 digit at a
    time.

    Args:
        first_num_string, second_num_string: String formated unsigned integers.
    Returns:
        Sum value as a string.
    """
    if digit_step < 1:
        raise ValueError('Invalid input argument.')

    result = ''
    power_of_10 = 10 ** digit_step
    carry = 0
    indices = [len(first_num_string), len(second_num_string)] 
    operands = [0, 0]
    number_strings = (first_num_string, second_num_string)
    while indices > [0, 0]:   
        for i in (0, 1):
            if indices[i] >= digit_step:
                operands[i] = int(number_strings[i][indices[i] - digit_step:
                                                    indices[i]])
                indices[i] -= digit_step

            elif indices[i] > 0:
                operands[i] = int(number_strings[i][:indices[i]])
                indices[i] = 0

            else:
                operands[i] = 0



        next_sum =  operands[0] + operands[1] + carry
        carry = next_sum // power_of_10
        if carry == 0 and indices[0] == 0 and indices[1] == 0:
            new_str_sum = str(next_sum % power_of_10)
        else:
            new_str_sum = str(next_sum % power_of_10).zfill(digit_step)
        result = new_str_sum + result

    if carry > 0:
        result = str(carry) + result

    return result
