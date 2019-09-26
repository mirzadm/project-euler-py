"""Project Euler: Problem 17"""


two_digit_base_words = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def two_digit_num_to_words(num):
    """Converts a 2-digit number `num` to its written words.

    Args:
        `num`: Integer between 0 and 99 (inclusive).
    Returns:
        Number writtin in words as a string.
    Raises:
        ValueError: For out of range `num`.
    """
    if num < 0 or num > 99:
        raise ValueError("Number must be between 0 and 1000.")

    if num in two_digit_base_words:
        words = two_digit_base_words[num]
    else:
        second_digit = num // 10
        tens = ""
        if second_digit:
            tens = two_digit_base_words[second_digit * 10]
        first_digit = num % 10
        ones = ""
        if first_digit:
            ones = two_digit_base_words[first_digit]
        if tens and ones:
            words = tens + " " + ones
        else:
            words = tens + ones

    return words


def three_digit_num_to_words(num):
    """Converts a 3-digit number `num` to its written words.

    Args:
        `num`: Integer between 0 and 999 (inclusive).
    Returns:
        Number writtin in words as a string.
    Raises:
        ValueError: For out of range `num`.
    """
    if num < 0 or num > 999:
        raise ValueError("Number must be between 0 and 1000.")

    third_digit = num // 100
    num = num % 100
    if third_digit:
        hundreds = two_digit_base_words[third_digit] + " hundred"
    tens_ones = two_digit_num_to_words(num)
    if third_digit and num:
        words = hundreds + " and " + tens_ones
    elif third_digit:
        words = hundreds
    else:
        words = tens_ones

    return words
