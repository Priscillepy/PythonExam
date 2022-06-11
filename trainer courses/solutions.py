# Problem 1: Write a function that reverses a string.
# Example:
#       input: "python"
#       output: "nohtyp"

import math
from datetime import date


def reverse_string(str):
    result = ""
    n = len(str)
    for i in range(n-1, -1, -1):
        result += str[i]

    return result


# Solving a quadratic equation

def quadratic_solution(a, b, c):
    if(a == 0):
        return "No solution"
    result = []
    d = math.sqrt(b*b - 4*a*c)
    result.append((-b+d)/(2*a))
    result.append((-b-d)/(2*a))
    return result


# Checking if string has unique characters

def has_unique_characters(str):
    n = len(str)
    for i in range(n):
        for j in range(i+1, n):
            if(str[i] == str[j]):
                return False
    return True

# Calculating age from string


def calculate_age(str):
    if(len(str) != 10):
        return "invalid input"
    # extracting day, month, year from string
    # dd-mm-yyyy
    #day = int(str[:2])
    month = int(str[3:5])
    year = int((str[6:]))
    # date of today
    today = date.today().strftime("%d-%m-%Y")
    #day_today = int(today[:2])
    month_today = int(today[3:5])
    year_today = int(today[6:])
    # differences
    year_diff = year_today - year
    if(year_diff < 0):
        return "incorrect birthday"
    month_diff = month_today - month
    if(month_diff < 0):
        year_diff -= 1
        month_diff = month_diff + 12
    str_month = "month"
    str_year = "year"
    # handling plurals
    if(month_diff > 1):
        str_month += "s"

    if(year_diff > 1):
        str_year += "s"

    return f"You are {year_diff} {str_year} and {month_diff} {str_month} old"


# print(reverse_string("python"))

#print(quadratic_solution(1, -5, 6))

# print(has_unique_characters("Python"))


# print(calculate_age("03-04-2000"))
