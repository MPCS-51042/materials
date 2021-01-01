
def compute_month_val(month, year):
    '''
    Determines the month value based on the month and year components.

    This function should return a value based on the table below and will require
    invoking the is_leap_year function:

    Month     | Return Value
    ----------|----------------------------
    January   | 0 ( 6 if year is a leap year)
    February  | 3 ( 2 if year is a leap year)
    March     | 3
    April     | 6
    May       | 1
    June      | 4
    July      | 6
    August    | 2
    September | 5
    October   | 0
    November  | 3
    December  | 5

    Inputs:
        month(int): A value [1-12] that represents a date's month
        year(int):  A value [1900-2020] that represents a date's year

    Outputs:
        Returns the integer based on the above table.
    '''
    pass


def compute_year_val(year):
    '''
    This function computes a value based on the years since the beginning of the
    century. Here are the steps to compute the return value:

      1. Extract the last two digits of the year. For example, If
             year = 2008
         then you would extract out 08 (a.k.a. 8)

     # 1 by 4. You only care about the integer portion so discard the decimal part.
     2. Divide the value from Step
        For example, if
            year = 2008
            Step #1 -> 8
            8/4 = 2
    3. Add the values from Step 1 and Step 2 together and return that value.

        Step #1 -> 8
        Step #2 -> 2

        return 8 + 2 = 10

    Inputs:
        year(int): A value [1900-2020] that represents a date's year

    Outputs:
        Returns the value computed from Step #3 from above.
    '''
    pass


def compute_century_val(year):
    '''
    This function computes the century based on the year component.
    Here are the steps to compute the return value:

    1. Extract out the first two digits of the year (i.e., century value). For example, if
         year = 2008

         century value = 20

    # 1 by 4 and record the remainder (Hint use the % operator). For example, if
    2. Divide the value from Step
         year = 2008
         Step #1 -> 20
         20 /4 = 5
         remainder = 0.

    # 2 from 3 and return this value multiplied by 2. For example, if
    3. Subtract the value from Step
          Step #2 -> 0
          return (3 - Step #2) * 2



    Inputs:
        year(int): A value [1900-2020] that represents a date's year

    Output:
        Returns the value computed from Step #3 from above.
    '''
    pass


def is_leap_year(year):
    '''
    Determines whether a year is a leap year

    Formula = ((year divisible by 400) or (year divsible by 4 and not divisible by 100))
    Hint: Use the % operator to check divisibility.

    Inputs:
        year(int): A value [1900-2020] that represents a date's year

    Output:
        Returns True if the year is a leap year otherwise false.
    '''
    pass


def is_valid_date(date):
    '''
    Determines whether the date is a valid. A valid date has the following format

        "month/day/year"

        month(int) -> Must be a value between [1-12] (i.e., inclusive) and the single digits can be written as
        01,02,03,04,05,06,07,08,09

        day(int) -> Must be a value between between [1-31] and the single digits can be written as
        01,02,03,04,05,06,07,08,09

        year(int) -> Must be a value between between [1900-2020].

        Make sure to check the following as well:

        1. If a month only has 30 days in it then day = 31 is invalid.
        2. Check to see if the year is a leap year. If the year is not a leap year then day = 29 is invalid.

    Inputs:
       date(str): The date as a string

    Outputs:
        From Professor Samuels: You can determine what you would like to return, a boolean, tuple, etc.
        It's up to you. Please remove this comment once you make a decision.
    '''
    pass


def find_day(dates):
    '''
    This function takes in a list of dates as strings. Each valid date will be in the following
    format:

          'month/day/year'

    This function only processes 'valid' date formats. Please check the is_valid_date function
    for the correct format (i.e.,  You should use this function within find_day).

    The find_day determines the day of the week (i.e. Sunday, Monday, Tuesday, Wednesday, ...)
    that each date falls on.

    Inputs:
        dates(list): A list of computed dates as strings

    Output:
        It converts each date inside the dates input into its day of the week and returns
        them as a list of strings. The day of the week must be in the same position that
        its date was in from the dates list. If a date is not a valid date then this function
        will generate 'error' as the value for that date.
    '''
    pass
