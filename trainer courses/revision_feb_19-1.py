# Variables
# Space reserved in the computer memory
# RAM: random access memory

# a = 4  # reserve memory space that I can access with the address 'a'
# # into that space, store 4 (00000000000....0100)
# # a is called the variable

# b = 7

# # print(a)


# a = "Python"

# print(a)


# Primitive Data Types
## Number, String, Boolean
# Number: int  (whole),  float (fraction), complex number
#         0, 1, 4, 6      1.5, 10.6
# String: text - in quotes ''  or ""

# first_name = "George's"
# last_name = "Brian"
# age = 16
# name = "My name"
# name = "The other name"
# c = 4.5

# Boolean variable can either take True or False
# is_adult = True
# is_teenager = False


# + for strings is concatenation
# print(first_name + ' ' + last_name + ' is ' + str(age))  # old syntax
#      George             Brian                   16
# Formatted String

#print(f"{first_name} {last_name} is {age} and he is in high school. ")


# String Methods
# methods are special functions in object-oriented programming

# Phone is an object
# properties [size, color, state, etc]
# behavior [switchOn, switchOff, etc]
# Phone.switchOn()

# print(first_name.upper())
# print(first_name.lower())

# Numbers

#  "30"+"30" = 3030
#

# x = input("Enter the value of x: ")
# y = input("Enter the value of y: ")

# name = input("Your name please: ")


# Always cast number inputs before manipulating them

# x = int(x)
# y = int(y)

# # You can cast an int to a float. But you cannot cast a float to an int

# # float -> int:  All ints are floats, but not all floats are ints
# # 2 = 2.0  (float),  2.3 != 2

# #z = x+y


# # add +
# print(f"{x} plus {y} is {x+y}")

# # subtract -
# print(f"{x} - {y} is {x-y}")

# # multiply *
# print(f"{x} multiplied by {y} gives {x*y}")

# # divide /
# print(f"{x} divided by {y} gives {x/y}")

# # whole number division: //
# print(f"The whole number when {x} is divided by {y} gives {x//y}")

# # Modulo %    (remainder when something is divided by another)
# # 3 divided by 2 = 1 r 1     3 mod 2 = 1.    4/2 = 2 r 0 -> 4 mod 2 = 0
# # 8 mod 3 = 2

# print(f"{x} modulo {y} is {x%y}")
# print(f"Your name is {name.upper()}")


# Control Flows
# Conditions
# Comparison operators

# equality ==  is equal to

# a = 5
# b = 4

# print(a == b)  # a is equal to b

# # not equal !=

# print(a != b)   # a is not equal to b

# # less than  <
# print(a < b)  # a is less than b

# # greater than >
# print(a > b)  # a is greater than b

# less than or equal to  <=
# greater than or equal to >=

# Conditional Statements

# if condition:
#    do this
# else:
#    do that


# Problem:
# Ask for the user's names, and print them if the user is at least 18 years
# Or tell the user that they're not eligible, if the age is less than 18

# adult_age = 18
# max_age = 50


# first_name = input("Whats your first name? >")
# last_name = input("Whats your last name?: ")
# age = input("Your age: >")

# # casting age to an integer
# age = int(age)

# # if age >= adult_age:
# #     print(f"Welcome to the program {first_name} {last_name}")
# # else:
# #     print("Sorry, you're not eligible for the program")

# # Many sub conditions

# age = int(age)

# if age < adult_age:
#     print(f"{first_name} {last_name}, you're too young for the program ")
# elif adult_age <= age <= max_age:
#     print(f"{first_name} {last_name}, you're welcome to the program ")
# else:
#     print(f"{first_name} {last_name}, you're too old for the program ")


# Chaining Operators

#  condition1 and condition2:  is true only when both conditions are true
# and is multiplication:  1 * 1 = 1,  1 * 0 = 0,  0 * 0 = 0

# f_numb = 10
# s_numb = 5
# t_numb = 2

# print(True and True)
# print(f_numb > s_numb and s_numb < t_numb)


# #  condition1 or condition2: is true if either of the conditions is true
# print(f_numb > s_numb or s_numb < t_numb)
# # or is addition:  1 + 0 = 1, 1 + 1 = 1 (logic), 0 + 0 = 0

# # condition1 and not condition2: is True if condition1 is True and condition2 is False

# print(f_numb > s_numb and not s_numb < t_numb)


# # condition1 or not condition2: is True if either condition1 is True or condition2 is False

# print(f_numb < s_numb or not s_numb > t_numb)
# # Brice: False
# # Walters: False
# # Priscille: False

# print((f_numb < s_numb or not s_numb > t_numb) or not s_numb < t_numb)


# Loops:
# names = ["John", "Paul", "Peter", "George"]

# print("John")
# print("John")
# print("John")
# print("John")
# print("John")

# For loop
# While loop


# for i in range(5):
#     print(i)

# for i in range(5, 10):
#     print(f"John - {i}")

# for i in range(1, 10, 2):
#     print(i)


# # [0, 1, 2, 3, 4]

# for i in ["John", "Peter", "Paul"]:
#     print(i)


# number_of_chances = 10

# while number_of_chances > 0:
#     print(number_of_chances)
#     number_of_chances = number_of_chances - 1


# while number_of_chances > 0:
#     if number_of_chances % 2 == 0:
#         print(number_of_chances)
#     number_of_chances = number_of_chances - 1

# Breaking the loop on a certain condition

# while number_of_chances > 0:
#     print(number_of_chances)
#     if(number_of_chances == 5):
#         break
#     number_of_chances -= 1


# while number_of_chances > 0:
#     print(number_of_chances)
#     number_of_chances -= 1

# Problem: Use the while loop to sum all the elements in a list

# numbers = [5, 7, 10, 2, 12, 10, 100, 13, 20, 5]
# 0  1  2   3  4,  5   6

# print(len(numbers))
# # end condition: when we have gone through all the elements

# print(numbers[4])

# solving the problme with a for-loop
# 0 1 2 3 4

import random
total = 0
product = 1

# for i in range(len(numbers)):  # [0, 1, 2, 3, 4]
#     total = total + numbers[i]

# for i in range(len(numbers)):  # [0, 1, 2, 3, 4]
#     product = product * numbers[i]
# range(6)  [0, 1, 2, 3, 4, 5]

k = 0
j = 0

# while k < len(numbers):
#     total = total + numbers[k]
#     k += 1
# # k = len(numbers)

# while j < len(numbers):
#     product = product * numbers[j]
#     j += 1


# How can you sum all the odd numbers in a list of numbers

# numbers = [5, 7, 10, 2, 12, 10, 100, 13, 20, 5]

# while k < len(numbers):
#     if numbers[k] % 2 == 0:
#         total = total + numbers[k]

#     k += 1


# print(total)

# Iterables

# names = ["Paul", "Joseph", "Brian"]

# [0, 1, 2, 3, 4]

# for i in range(5):
#     print(i)

# for name in names:
#     print(name)

# For... Else

# for i in range(5):
#     if i != 3:
#         print(i)
#     else:
#         print("I found 3")
#         break


# Nested loop = a loop inside a loop

# names = ["Mary", "Stephanie", "John"]
# numbers = [2, 3, 4]

# # for name in names:
# #     for number in numbers:
# #         print(f"{name} - {number}")


# for i in range(len(names)):
#     print(f"{numbers[i]} - {names[i]}")


# You're given a list of numbers
# Write a program that detects whether there are any duplicates

students = ["Mary", "Stephanie", "John",
            "Paul", "John", "Claude", "Peter", "Paul"]

# Algorithm
# Step1: assume number_of_students = len(students)
# Step2: loop through the list and each time you detect a duplicate, decrement number_of_students by 1
# Step3: Print the final number_of_students

# Step 2: We take each element on the loop and compare with other elements.
#        If any of the other elements is equal to our initial element, then there is a duplicate


# number_of_students = len(students)

# for i in range(number_of_students):  # [0, 1, 2, 3, .....8]
#     for j in range(i+1, number_of_students):  # [1, 2, 3, ....8]
#         if students[i] == students[j]:
#             print(f"We found a duplicate: {students[i]}")
#             break


a = [1, 2, 3]
b = [5, 6, 7]

for i in range(len(a)):
    for j in range(len(b)):
        print(a[i], b[j])

# Mary - Stephanie
# Mary - John
# Mary - Paul
# ...
# Mary - John

# Stephanie - John
# Stephanie - Paul


# John - Paul
# John - John   # Declare that there's a duplicate
