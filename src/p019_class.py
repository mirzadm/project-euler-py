

class Date:
    def __init__(year, month, day):
        if month < 1 or month > 12:
            raise ValueError("Month out of range.")

        self.year = year
        if 

    def is_valid(year, month, day):
        if day < 1 or month < 1 or month > 12:
            return False
        

    def is_leap_year(year):
        return year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)

    def days_in_year(year):
        return 366 if is_leap_year(year) else 365


    def days_in_month(month, year=0):
        """Returns number of days in `month`. Handles leap year.

        Args:
            `month`: Integer between 1 and 12.
            `year`: Non-negative integer.
        Returns:
            Number of days in month.
        Raises:
            ValueError: Out of range `month` or `year`.
        """
        if month < 1 or month > 12:
            raise ValueError("Month or year value out of range!")

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
