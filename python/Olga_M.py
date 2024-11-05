# HW1 Convert C to F
Temperature = input("What do you want to convert? \n1 Celsius to Fahrenheit: \n2 Fahrenheit to Celsius: \n ")

if Temperature == "1":
    Celsius = float(input("Enter temperature in Celsius: \n"))
    Fahrenheit = (Celsius * 1.8) + 32
    print(Fahrenheit)
elif Temperature == "2":
    Fahrenheit = float(input("Enter temperature in Fahrenheit: \n"))
    Celsius = (Fahrenheit - 32) / 1.8
    print(Celsius)
else:
    print("Wrong input, please try again.")

# Convert kg to lb
Weight = input("What do you want to convert? \n1 Kilogram to Pounds: \n2 Pounds to Kilogram: \n ")

if Weight == "1":
    Kilogram = float(input("Enter weight in lb: \n"))
    Pounds = Kilogram * 2.20462
    print(Pounds)
elif Weight == "2":
    Pounds = float(input("Enter weight in kg: \n"))
    Kilogram = Pounds * 0.45359
    print(Kilogram)
else:
    print("Wrong input, please try again.")


# Variables
# print("Hello World!")

# first_name = "Olga"  # string <-between quotes
# last_name = "Markova"
# price = "19"
# price_2 = "3"
# age = 26    # integer
# age_2 = 3
# city = "San Francisco"
# temperature = 18.5   # float
# temperature_2 = 5
#
# print(int(price) - int(price_2))
#
# print(age)
# print(type(str(age)))        # converted from int to str

# Explanation -inside out:
# age_str = str(age)
# type_of_age = type(age_str)
# print(type_of_age)


# c = age / 2    -> when divide it's float
# print(c)
# print(type(c))

# print(age + age_2)
# print(temperature + temperature_2)
# print(price + price_2)
# print(first_name, last_name)

# print(first_name)
# print(last_name)
# print(type(first_name))
# print(price)
# print(type(price))
# print(age)
# print(type(age))
# print(city)
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
# elif answer_3 == "/":
#     print(answer_1 / answer_2)
# elif answer_3 == "*":
#     print(answer_1 * answer_2)
# else:
#     print("Wrong input")
#
# print("Done!")


# answer = input("Choose \n1 to convert km -> miles: \n2 to convert miles -> km: ")
#
# if answer == "1":
#     km = float(input("Enter km: "))
#     miles = km / 1.609
#     print(miles)
# elif answer == "2":
#     miles = float(input("Enter miles: "))
#     km = miles * 1.609
#     print(km)
# else:
#     print("Wrong input please try again")
