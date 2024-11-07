# print("Hello World!")

# first_name = "Andrey"
# last_name = 'Baykov'
# price = "18"
# price_2 = "3"
# age = 26
# age_2 = 2
# temperature = 17.5
# temperature_2 = 5
#
# print(int(price) - int(price_2))
#
# print(age)

# age_str = str(age)
# type_of_age = type(age_str)
# print(type_of_age)

# print(type(str(age)))

# c = age / 2
#
# print(c)
# print(type(c))

# print(age + age_2)
# print(temperature + temperature_2)
# print(price + price_2)
# print(first_name, last_name)
#
# print(first_name)
# print(type(first_name))
# print(last_name)
# print(price)
# print(type(price))
# print(age)
# print(type(age))
# print(temperature)
# print(type(temperature))

# answer_1 = int(input("Enter first number: "))
# answer_2 = int(input("Enter second number: "))
# answer_3 = input("Enter operation [+, -, /, *]: ")
#
# if answer_3 == "+":
#     print(answer_1 + answer_2)
# elif answer_3 == "-":
#     print(answer_1 - answer_2)
# elif answer_3 == "*":
#     print(answer_1 * answer_2)
# elif answer_3 == "/":
#     print(answer_1 / answer_2)
# else:
#     print("Wrong input")
#
# print("Done!")

answer = input("Choose \n1 to convert km -> miles \n2 to convert miles -> km: ")

# a == b
# a < b
# a > b
# a <= b
# a >= b
# a != b


# if answer == "1":
#   km = float(input("Enter km : "))
#  miles = km / 1.609
# print(miles)
# elif answer == "2":
#    miles = float(input("Enter miles : "))
#    km = miles * 1.609
#    print(km)
# else:
#   print("Wrong input please try again")

# (c * 9/5)+32 = f
# (f - 32) * 5/9 = c

# Instructions: need enter Type f== "fahrenheit" c== "celsius" and then need to enter number

degreesType = input("type of degree: ")
if degreesType == "f":
    a = int(input("Pleas enter degree number: "))
    print((a * 9 / 5) + 32)
elif degreesType == "c":
    b = int(input("Pleas enter degree number: "))
    print((b - 32) * 5 / 9)
elif degreesType != "f" and degreesType != "c":
    print("Invalid input")

if answer == "1":
    km = float(input("Enter km (0 - 1000): "))
    if km < 0 or km > 1000:
        print("Value out of range")
    else:
        miles = km / 1.609
        print(miles)
elif answer == "2":
    miles = float(input("Enter miles (0 - 1000): "))
    # if miles >= 0:
    if miles >= 0 and miles <= 1000:
        km = miles * 1.609
        print(km)
    else:
        print("Value out of range")
else:
    print("Wrong input please try again")

a:  bool = True
b:  bool = False
#
# # AND
# True True = True
# False True = False
# True False = False
# False False = False
#
# # OR
# True True = True
# False True = True
# True False = True
# False False = False
#
# # NOT
# not True = False
# not False = True



answer = input()

