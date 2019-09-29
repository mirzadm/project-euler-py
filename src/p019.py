"""Project Euler: Problem 19"""


def number_of_first_of_month_sundays_in_20th_century():
    num_sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if year == 1901 and month == 1:
                # 1901-01-01 given 1900-01-01 is Monday and 1900 not a leap year.
                curr_day = 1 + 365
            else:
                prev_month = (month - 1) or 12
                days_in_prev_month = days_in_month(prev_month, year)
                curr_day = (curr_day + days_in_prev_month) % 7
                if not curr_day:
                    num_sundays += 1
    return num_sundays


def is_leap_year(year):
    return year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)


def days_in_year(year):
    return 366 if is_leap_year(year) else 365


def days_in_month(month, year=0):
    """Returns number of days in `month`. Handles leap year.

    Args:
        `month`: Integer between 1 and 12.
        `year`: Integer.
    Returns:
        Number of days in month.
    Raises:
        ValueError: Out of range `month`.
    """
    if month < 1 or month > 12:
        raise ValueError("Month value out of range!")

    months_with_31_days = (1, 3, 5, 7, 8, 10, 12)
    months_with_30_days = (4, 6, 9, 11)
    if month in months_with_31_days:
        return 31
    if month in months_with_30_days:
        return 30
    # Februery
    if is_leap_year(year):
        return 29
    else:
        return 28
