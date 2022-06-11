# # Lists
# # Definition

# students = ["Paul", "Bertrand", "Peter"]  # list of strings
# numbers = [1, 4, 2, 7, 5]   # list of numbers
# matrix = [[1, 2], [3, 4], [5, 6]]   # list of lists - 2 dimensional list
# zeros = [0]*10
# students_numbers = students + numbers   # creating a list from 2 sub-lists
# numbers_to_twenty = list(range(20))  # 0, 1, ........ 19
# chars = list("Hello my friend")  # splitting a string

# # print(students)
# # print(numbers)
# # print(matrix)
# # print(zeros)
# # print(students_numbers)
# # print(numbers_to_twenty)
# # print(chars)

# # Number of items in a list
# # print(len(students))
# # print(len(matrix))

# # Accessing Lists
# #  - Accessing Lists
# #             - list1[index], list1[-1]
# #             - list1[index] = new_value
# #             - list1[0:index], list1[:index], list1[0:], list1[:], list1[::2], list1[::-1]

# print(students[0])
# print(students[-1]) # last
# print(students[0:2]) # 0, 1
# print(matrix[0:2])
# print(students[0:])  # every item to the right of first index inclusive
# print(students[1:])
# print(students[:2]) # [0:2]
# print(students[:])  # making a copy of the students list
# print(students[::2])
# print(students[::-1])  # reverse a list

# # Modifying an element in the list

# students[1] = "Brice"
# print(students)


# Unpacking Lists
#  - List Unpacking
#             - var1, var2, var3 = list1
#             - var1, var2, *other = list1
#             - first, *other, last = list1


# students = ["Paul", "Bertrand", "Peter", "Joseph", "Claude", "Priscille"]
# numbers = [1, 4, 2, 7, 5]


# # first = students[0]
# # second = students[1]
# # third = students[2]
# # last = students[-1]

# first, second, third, *others = students

# # print(others)

# item1, item2, *other_items, last_but_one, last_item = students

# print(last_but_one)
# print(other_items)


# Looping through Lists

# - Looping over Lists
#     - for letter in list1:
#     - for letter in enumerate(list1): print(letter[0], letter[1])
#     - for index, letter in enumerate(list1):

# students = ["Paul", "Bertrand", "Peter", "Joseph", "Claude", "Priscille"]

# # for student in students:
# #     print(student)

# # what if we want the indices of each element
# # print(list(enumerate(students)))

# # for student in enumerate(students):
# #     print(student[0], student[1])

# for index, student_name in enumerate(students):
#     if(index <= 2):
#         print(index, student_name)


# Adding and Removing items
# - Adding or Removing Items
#     - Add: list1.append(item)
#             list1.insert(0,item)
#     - Remove: list1.pop()
#                 list1.pop(index)
#                 list1.remove(item) -- removes first occurence of item
#                 del list1[index],  del list1[0:index]
#                 list1.clear()

from pprint import pprint
from array import array
from collections import deque
students = ["Paul", "Bertrand", "Peter",
            "Joseph", "Claude", "Priscille"]
# Adding items

# students.append("Walters") # add item at the end of the list
# print(students)
# students.insert(3, "Brice") # add item at any index position
# print(students)

# Removing items

# removed_name = students.pop()
# print(removed_name)
# print(students)

# # removes first instance of item (given the name of item)
# students.remove("Peter")
# print(students)

# del students[:3]

# students.pop(3)

# del students[3]

# students.clear()

# print(students)

# students = ["Paul", "Bertrand", "Peter",
#             "Joseph", "Claude", "Priscille"]

# students.clear()
# students.append("Paul")
# students.pop()

# print(students)


# Finding Items
# - Finding Items
#     - list1.index(item)
#     - if item in list1: print(list1.index(item))
#     - list1.count(item)

# students = ["Paul", "Bertrand", "Peter",
#             "Joseph", "Claude", "Priscille", "Paul"]

# print(students.index("Claude"))

# # Problem: delete Joseph from the list
# index = students.index("Joseph")
# # del students[index]
# students.pop(index)
# print(students)

# students.remove("Paul")

# if "Mary" in students:
#     index = students.index("Mary")
#     students.pop(index)

# print(students)

# Prob: how to remove item when it repeats

# students.remove("Paul")
# print(students)

# for student in students:
#     if(student == "Paul"):
#         students.remove(student)

# print(students)

# Prob: swap second and third element

students = ["Paul", "Bertrand", "Peter",
            "Joseph", "Claude", "Priscille"]

# temp = students[1]
# students[1] = students[2]
# students[2] = temp

# my_list = [students[0:2], students[2:]]

# Sorting Lists
# - Sorting Lists
#     - numbers.sort()
#     - numbers.sort(reverse=True)
#     - sorted(numbers, reverse=True)

# # students.sort() # sorting in ascending order
# numbers = [4, 1, 3, 8]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)

# # students.sort(reverse=True)  # sort in descending order
# sorted_students = sorted(students, reverse=True)  # sort in descending order
# print(sorted_students)

# Prob: Display the products in descending order of prices

# products = [("orange", 100), ("apple", 150), ("biscuits", 25), ("bread", 200)]

# products.sort(reverse=True)
# sorted_products = sorted(products)

# def sort_items(item):
#     return item[1]

# products.sort(key=sort_items, reverse=True)

# Lambda functions
# A function passed inside another function
# lambda parameters: expression

# products.sort(key=lambda product: product[1], reverse=True)

# Sort this from the most recent expiry date to the least recent

products = [("orange", 100, "6-8-22"), ("apple", 150, '3-8-22'),
            ("biscuits", 25, "1-8-22"), ("bread", 200, "9-8-22")]

# products.sort(key=lambda product: product[2], reverse=True)

# Mapping

# Prob: how can we extract only product names from the products list?
# Method 1: using loop
# product_names = []
# for product in products:
#     product_names.append(product[0])

# Method 2: using map() function
# map(lamda-function, list)

# product_names = list(map(lambda product: product[0], products))


# # Filtering
# # Prob: What if we only want products whose prices are greater than or equal to 100
# # method 1: use loop
# # expensive_products = []
# # for product in products:
# #     if product[1] >= 100:
# #         expensive_products.append(product)

# expensive_products = list(filter(lambda product: product[1] >= 100, products))


# List Comprehensions
#  - prices = [item[1] for item in items]
# expression for product in products
# Mapping
# product_names = [product[0] for product in products]
# # Filtering
# expensive_products = [product[0] for product in products if product[1] >= 100]


# print(expensive_products)


# Zip function: combines lists item by item

# names = ["Paul", "John", "Peter", "Junior"]
# ages = [25, 15, 32, 12]


# print(list(zip(names, ages)))


# Stacks

# Creating a Stack

# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack)
# stack.pop()


# print(stack)
# stack.pop()
# print(stack)
# print(stack[-1])

# Stacks have 2 methods
# append()
# pop()


# Queues
# Create

# from collections import deque

# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)

# print(queue)
# queue.popleft()
# print(queue)
# queue.popleft()
# print(queue)


# Tuples
# Read-only

# point_1 = (1, 3)
# point_2 = (4, 5)

# print(point_1 + point_2)

# list_1 = list(point_1)

# list_1[0] = 7
# print(list_1)

# point_1 = tuple(list_1)
# print(point_1)


# list()
# tuple()

# point_3 = tuple([4, 5, 8, 9])

# print(point_3)


# Swapping elements in an array


# temp = my_list[1]
# my_list[1] = my_list[2]
# my_list[2] = temp
# [a,b] = [b,a]

# [my_list[1], my_list[2]] = [my_list[2], my_list[1]]

# print(my_list)


# def swap_list(my_list):
#     result = []
#     n = len(my_list)
#     for i in range(n-1, -1, -1):
#         result.append(my_list[i])
# #     return result

# def swap_list_inplace(my_list):
#     n = len(my_list)
#     for i in range(0, (n//2)):

#         [my_list[i], my_list[n-i-1]] = [my_list[n-i-1], my_list[i]]
#         # temp = my_list[i]
#         # my_list[i] = my_list[n-i-1]
#         # my_list[n-i-1] = temp
#     return my_list

# # # 0   n-1 = n-0-1
# # # 1   n-2 = n-1-1
# # # 2   n-3 = n-2-1

# # # i    n-i-1


# # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# name_list = ["Paul", "Sandra", "John", "Pierre", "George"]

# print(swap_list_inplace(name_list))


# my_array = array("i", [1, 2, 3, 4])

# # print(my_array)

# for i in my_array:
#     print(i)

# Sets
# list of unique values

a = {1, 2, 3}
b = {3, 4, 5}


# a.add(6)
# a.add(2)

# print(a)

# len(a)

# intersection, union, XOR (exclusive union)

# union

# print(a | b)

# # intersection

# print(a & b)

# # exclusive OR

# print(a ^ b)

# l1 = ["Paul", "John", "Peter", "Mary", "John"]
# l2 = ["Peter", "Mary", "Michael"]

# print(set(l1) | set(l2))


# Dictionary

# d = {"x": 2, "y": 5}  # keys must be immutable: string, number
# e = dict(x=4, y=5, z=8)

# # print(d["x"])
# # print(d)
# # print(e)

# # for key, value in e.items():
# #     print(key, value)


# set_1 = {x*2+1 for x in range(11)}

# dict_1 = {x: x*2 for x in range(11)}
# dict_2 = {x: x*2+1 for x in range(11)}

# dict_3 = {**dict_1, **dict_2}

# # # print(set_1)
# # print(dict_1)

# # print(dict_2)

# print(dict_3)

# Example: Given a string, find the most repeated character.
# Algo: count the freq of each char - store it in a dictionary


def most_repeated_character(sentence):
    dictionary = {}
    for char in sentence:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    sorted_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    sorted_filtered_list = list(filter(lambda x: x[0] != " ", sorted_list))
    return sorted_filtered_list[0][0]


sentence = "This is an example of a sentence insideoo here. So another only only stuff . o o o, the o"


print(most_repeated_character(sentence))
