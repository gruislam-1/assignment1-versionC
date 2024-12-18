#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py
The python code in this file is original work written by
"G.M. REZWAN UL ISLAM". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: G.M. REZWAN UL ISLAM
Semester: Fall 2024
Description: Assignment 1_Version C
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]


def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    lyear = year % 4
    if lyear == 0:
        leap_flag = True # this is a leap year
    else:
        leap_flag = False # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True # this is a leap year

    return leap_flag # will return True if it is a leap year


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} # days in relation to each month

    leap_flag = leap_year(year) # leap year check

    if month == 2 and leap_flag: # check month of February for leap year
        return 29
    else:
        return mon_dict[month]


def after(date: str) -> str:
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    leap_flag = leap_year(year) # leap year check

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]

    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1
    return f"{day:02}/{mon:02}/{year}"


def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # previous day

    if day == 0:
        mon -= 1 # go to previous month
        if mon == 0:
            year -= 1 # go to previous year
            mon = 12 # month is set to December

        if mon == 2: # checking for leap year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day = 29
            else:
                day = 28
        else:
            mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            day = mon_dict[mon]
    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    print("The date and/or number is invalid")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    date_parts = date.split('/')  # split date into parts

    if len(date_parts) != 3:  # check for three parts format (day, month, year)
        return False # if date not three parts format return "False"

    day_str, mon_str, year_str = date_parts # strings of day, month, year

    # check day, month, year = digits/numbers
    day_is_digit = day_str.isdigit()
    month_is_digit = mon_str.isdigit()
    year_is_digit = year_str.isdigit()

    # return False/Invalid if day, month, year are not digits/numbers
    if day_is_digit == False:
        return False
    if month_is_digit == False:
        return False
    if year_is_digit == False:
        return False

    # day, month, year to integers
    day = int(day_str)
    mon = int(mon_str)
    year = int(year_str)

    if mon < 1: # checking if month number is less than 1 = invalid
        return False
    if mon > 12: # checking if month number greater than 12 = invalid
        return False

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # number of days in month

    if (year % 4 == 0 and year % 100 != 0):
        days_in_month[1] = 29  # leap year for February
    else:
        if year % 400 == 0:
            days_in_month[1] = 29  # leap year for February

    if day < 1: # checking for valid days of the month
        return False
    if day > days_in_month[mon - 1]: # checking for valid days of the month
        return False

    return True  # if date is valid return "True"


def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    date = start_date

    while num != 0:
        if num > 0:
            date = after(date)  # go to next day
            num -= 1  # decrement of num by 1
        else:
            date = before(date)  # go to previous day
            num += 1  # increment of num by 1

    return date


def valid_number(num: str) -> bool:
    """
    check that second argument is a valid number (+/-)
    """
    if num[0] == '-':  # to check if number starts with a negative ('-') sign/o>
        return num[1:].isdigit()  # to check if the other strings are digit/num>
    return num.isdigit()  # check if all the strings are numbers/digits


if __name__ == "__main__":
    if len(sys.argv) != 3: # check length of arguments
        usage()

    start_date = sys.argv[1]
    num_days_str = sys.argv[2]

    if valid_date(start_date) == False: # check first arg is a valid date
        usage()

    if valid_number(num_days_str) == False: # check that second arg is a valid number (+/-)
        usage()

    num_days = int(num_days_str) # convert second argument to integer "int()"

    end_date = day_iter(start_date, num_days) # call day_iter function to get and save the end date

    week_day = day_of_week(end_date) # call the day_of_week function to get the day (Mon, Tue, etc.) of end date

    print(f"The end date is {week_day}, {end_date}.") # print(f'The end date is {day_of_week(x)}, {x}.')

    pass
