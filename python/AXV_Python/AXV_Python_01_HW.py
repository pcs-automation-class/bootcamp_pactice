# This program is for temperature conversion from Celsius to Fahrenheit
# and from Fahrenheit to Celsius

response = input("Choose \n1 to convert Fahrenheit to Celsius \n2 to convert Celsius to Fahrenheit: ")

if response == "1":
    fahrenheit = (float(input("Enter Fahrenheit: ")) - 32) * 5/9
    print(fahrenheit)
elif response == "2":
    celsius = ((float(input("Enter Celsius: "))) * 9/5) + 32
    print(celsius)
else:
    print("Invalid Value!  Please start over!")
