# for

# for number in range(100):
#     print(number)

# name = "Andrey"
# for letter in name:
#     print(letter)

# while
# i = 15
#
# while i > 10:
#     i -= 1
#     if i == 13:
#         break
#         # continue
#     print(i)
#     # i = i - 5

# h = 0
#
# while h < 15:
#     h += 1
#     if h == 13:
#         # continue
#         break
#     print(h)
#
# while True:
#     letter = input('Enter a letter: ')
#     print(letter)
#     if letter == "q":
#         break

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
def print_result(number):
    print("Result: " + str(number))
    print_line_of_asterix()


def print_line_of_asterix():
    print("******************")



one = int(input("Enter a number: "))
two = int(input("Enter a number: "))

result = one + two
print_result(result)

result = one - two
print_result(result)

result = one * two
print_result(result)

result = one / two
print_result(result)


