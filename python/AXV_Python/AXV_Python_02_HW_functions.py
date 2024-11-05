#calculator function

def axv_calc(mathematical_operation, num1, num2):
    if mathematical_operation == 'add':
        return num1 + num2
    elif mathematical_operation == 'subtract':
        return num1 - num2
    elif mathematical_operation == 'multiply':
        return num1 * num2
    elif mathematical_operation == 'divide':
        if num2 !=0:
            return num1 / num2
        else:
            return "You cannot divide by zero!"
    else:
        return ("This operation is not supported")

mathematical_operation = input("Enter the operation (add, subtract, multiply, divide): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = axv_calc(mathematical_operation, num1, num2)
print(result)

#Calculate temperatures from Farhrenheit to Celcius and from Celcius to Fahrenheit

def temp_calc(math_calc, temperature):
    math_calc = math_calc.lower()
    if math_calc == 'c':
       return ((temperature * 9/5) + 32)
    elif math_calc == 'f':
        return ((temperature - 32) * 5/9)
    else:
        return ("Invalid Operation!")

math_calc = input("Enter 'c' for Celsius or 'f' for Fahrenheit: ")
temperature = float(input("Please enter temperature: "))

result = temp_calc(math_calc, temperature)
print(result)

#Convert speed/distance from miles to kilometers and from kilometers to miles
def speed_calc(speed_mi_or_km, speed):
    speed_mi_or_km = speed_mi_or_km.lower()
    if speed_mi_or_km == 'k':
        return (speed * 0.621371)
    elif speed_mi_or_km == 'm':
        return (speed * 1.60934)
    else:
        return ("Invalid Operation!")

speed_mi_or_km = input("Enter 'k' for kilometers or 'm' for miles: ")
speed = float(input("Please enter speed in to convert: "))
result = speed_calc(speed_mi_or_km, speed)
print(result)

# response = input("Choose \n1 to convert Fahrenheit to Celsius \n2 to convert Celsius to Fahrenheit: ")
#
# if response == "1":
#     fahrenheit = (float(input("Enter Fahrenheit: ")) - 32) * 5/9
#     print(fahrenheit)
# elif response == "2":
#     celsius = ((float(input("Enter Celsius: "))) * 9/5) + 32
#     print(celsius)
# else:
#     print("Invalid Value!  Please start over!")





# def axv_function():
#     print("Anna's function")
#     name = input("Enter your name:\n")
#     print(f"Hello {name}")
# axv_function()

#axv_function
# def axv_function():
#     print("Hello from Anna's function")
# axv_function()

#arguments
# def my_function(axv_function):
#     print(axv_function + " Vaysman")
#
# my_function("Anna")
# my_function("Raisa")

# def my_function(first_name, last_name):
#     print(first_name + " " + last_name)

# my_function("Anna", "Vaysman")
# my_function("Samuel", "Sharivker")
# my_function("Alexander", "Sharivker")
# my_function("Raisa", "Vaysman")

# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(city):
#     for x in city:
#         print(x)
#
# cities = ("New York", "Los Angeles", "Milan", "Florence")
# my_function(cities)

# def my_function(x):
#     return 5 * x
# print(my_function(0))
# print(my_function(1))
# print(my_function(2))
# print(my_function(3))
# print(my_function(4))
# print(my_function(5))

