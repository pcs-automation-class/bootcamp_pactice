# "FOR" loop - we know how many times it will run

# for number in range(10):
# # values 0 to 9 --> total of 10 numbers
#     print(number)

# name = 'Samuel Joseph'
# for letter in name:
#     print(letter)

# "WHILE" Loop - needs to have a condition to stop it

# i = 5
# while i < 10:
#     print(i)
# #    i = i + 1
#     i += 2
#
# i = 15
# while i > 10:
#     print(i)
# #    i = i - 1
#     i -= 1

# it is better to use shorter version such as i -= x or i += x

# i = 50
# while i > 10:
#     print (i)
#     i -= 1
#     if i == 35:
# # break command stops "while" loop
#         break

# i = 20
# while i > 10:
#     i -= 1
#     if i == 13:
#         # break command stops "while" loop
#         continue
#     print (i)

# while True:
#     letter = input("Enter a letter: ")
#     if letter == 'q':
#         break
#     print(letter)

#this is an endless loop:
# while True:
#     letter = input('Enter a letter: ')
#     if letter =='q':
#         continue
#     print(letter)

# for j in range(15):
#     if j == 4:
#         #this will skip 4
#         continue
#     print(j)
#
# for j in range(15):
#     if j == 4:
#         break
#     print(j)

# while True:
#     print(2)
#     break
#
# while True:
#     #enter your calculator code here
#     print("my calculator")
#     #
#     answer = input("Do you want to continue? (y/n): ")
# #    if answer.lower() == 'n':
# #    if answer.upper() == 'N':
#     if answer.title() == 'No':
#         break
#
# #Reusable code

def print_result(result):
    print("Result = " + str(result))
    print('**********')

# Input numbers
one = int(input("Enter 1st number: "))
two = int(input("Enter 2nd number: "))

# Calculate the result
result = one + two

# Print the result using the function
print_result(result)

result = one - two
#print("Result = " + str(result))
print_result(result)

result = one * two
# #print("Result = " + str(result))
print_result(result)
#

if two == 0:
    print("Cannot divide by zero")
else:
    result = one / two
    print_result(result)
#print("Result = " + str(result))
