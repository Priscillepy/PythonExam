# file = open("data.txt", "w")
# file.write("My data")

# Print numbers from 1 to 5
# using for loop

# for i in range(5):  # 0, 1, 2, 3, 4
#     print(i+1)

# print("End of for loop")
# k = 0

# while k < 5:
#     print(k+1)
#     k += 1

# Use while loop: A program where we cannot tell how many times the loop will run


# while True:
#     number = input("Enter a number: ")
#     number = int(number)
#     if number == 140:
#         break

# for i in range(10):
#     num = input("Enter a number: ")
#     num = int(num)
#     if num == 140:
#         break


# ***** Functions

# Purpose of functions: ensure code clarity and reusability

# a = [1, 2, 3, 10, 12]

# len(a)

# Categories
# - Built-in functions
# - Custom functions
#  - create your own
#  - use those created by other developers  [modules/packages]

# Creating a function


def greet(name):
    print(f"Good morning {name}")
    print("You're welcome")


def is_adult(age):
    age = int(age)
    if age >= 18:
        return True
    else:
        return False


# name = input("What's your name? ")
# user_age = input("What's your age ")

# if is_adult(user_age):
#     greet(name)


# parameters vs arguments
#   defining |    calling

# Two types of functions:
#  - perform a task
#  - return a value

# adult = is_adult(12)
# b = greet("Paul")

# print(is_adult(35))

# print(greet("Paul"))

# a = print("Text")
# b = len([0, 2, 4])

# print(a)
# print(b)


# Keyword arguments

def increment(num, by):
    return num + by


def increment_by_two(num, by=2):
    return num + by


# Default arguments  : how do we make arguments optional

# xargs - Multiple arguments

def multiply(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# new_value = multiply(10, 15, 2)


# print(multiply(10, 15, 2))


# xxargs - Multiple arguments in form of key=value pairs

# def save_user(**user):
#     file = open("data.txt", "w")
#     file.write(str(user))
#     print(user)


# name = input("Enter user's name: ")
# age = input("Enter user's age: ")
# address = input("Enter user's address")
# save_user(user_name=name, user_age=age, user_address=address)


# Scope
# in which area of my code is a given variable defined/visible ?
# 2 types of scopes
# -local
#   - any variable defined inside a function is only visible inside that function
# -global
#   - if a variable is defined outside a function, it is global

# name = "Thomas"


# def greetings(name):
#     #name = "Peter"
#     print(f"Welcome {name}")

#     for i in range(4):
#         print(i)


# greetings("Peter")

# print(f"Welcome {name}")

# Exercises
# 1. Write a function that detects if a number is a prime number:  is_prime(n)
#    Example: if the function receives 7, it returns True. If it receives 10, it returns False

# A prime number is a number that only divides itself and one.
# -> if a given number is divisible by any other number apart from 1 and itself, then
#    it is not prime

# 2. Write a function that solves a quadratic equation

# if variable % 2 ==0 return False    9
# if variable ==2 return True


# 1]  2, 3, 4, 5, 6, 7, 8, 9, 10, 11

# 1. Conception: conceiving a solution (algo)
# Given a number n, check if n is divisible by any number less than n and different from 1
# if it happens, then n is not a prime number. Else then n is a prime number

# Implementation
# 7: 6, 5, 4, 3, 2 = range(2, 7)
# 9: 8, 7, 6, 5, 4, 3, 2 = range(2, 9)
# n: range(2,n)

# Given n, generate a range of numbers between 2 and n. Check if there exist any number
# in this range that divides n. If it exists, then n is not prime. If we cannot find any
# in this range that divides n, then n is prime.


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            print(f"{n} is NOT a prime number because it is divisible by {i}")
            return False
    print(f"{n} is a prime number")
    return True


# number = input("Enter a number: ")
# number = int(number)

print(is_prime(39))
