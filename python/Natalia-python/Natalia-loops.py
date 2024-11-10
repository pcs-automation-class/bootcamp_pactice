# import math
from math import sqrt

# h = 0

# while h < 15:
#     h += 1
#     if h == 13:
#         # continue
#         break
#     print(h)
#
#

# while True:
#     letter = input('Enter a letter: ')
#     if letter == "q":
#         continue
#     print(letter)


# for j in range(15):
#     if j == 4:
#         break
#     print(j)

#
# while -1:
#     print(1)
#     break

# while True:
#     # calculator
#     print("my calculator")
#     #
#     answer = input("Do you want to continue? (y/n) : ")
#     # if answer.title() == "N":
#     #     break
#     if answer != "y":
#         break
#
#         # Exit  exit eXit => EXIT
#

# Don't
# Repeat
# Yourself

#=====================
# functions
# def print_result(number):
#     print("Result: " + str(number))
#     print_line_of_asterix()
#
#
# def print_line_of_asterix():
#     print("******************")
#
#
#
# one = int(input("Enter a number: "))
# two = int(input("Enter a number: "))
#
# result = one + two
# print_result(result)
#
# result = one - two
# print_result(result)
#
# result = one * two
# print_result(result)
#
# result = one / two
# print_result(result)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(7):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

def calculation(num_1, num_2, sign):
    if sign == '+':
        return num_1 + num_2
    elif sign == '-':
        return num_1 - num_2
    elif sign == '*':
        return num_1 * num_2
    elif sign == '/':
        return num_1 / num_2
    elif sign == '^':
        return sqrt(num_1)


while True:
    answer_1 = int(input("Enter first number: "))
    answer_2 = int(input("Enter second number: "))
    answer_3 = input("Enter sign +, -, / , *): ")

    result = calculation(answer_1, answer_2, answer_3)
    print(result)

    if input("Would you like to continue? [Y/N]: ").upper() != 'Y':
        break
