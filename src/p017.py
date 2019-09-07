"""Project Euler: Problem 16"""


num_to_words_map = {
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
    1000: "thousand",
}


def num_to_words(num):
    """Converts a number `num` to its written words.

    Args:
        `num`: Integer between 0 and 1000 (inclusive).
    Returns:
        Number writtin in words as a string.
    Raises:
        ValueError: For out of range `num`.
    """
    if num < 0 or num > 1000:
        raise ValueError("Number must be between 0 and 1000.")

    if num == 0:
        return "zero"
    if num == 1000:
        return "one thousand"

    words = ""
    thrid_digit = num // 100
    second_digit = (num % 100) // 10
    first_digit = num % 10

    if thrid_digit:
        words = num_to_words_map[thrid_digit] + " hundred"
        if second_digit or first_digit:
            words += " and "

    if second_digit == 1:
        words += num_to_words_map[second_digit * 10 + first_digit]
    elif second_digit:
        words += num_to_words_map[second_digit * 10]
        if first_digit:
            words += " "

    if first_digit and second_digit != 1:
        words += num_to_words_map[first_digit]

    return words
