answer = input("Choose \n1 to convert celsius -> fahrenheit, 2 to convert fahrenheit -> celsius: ")
if answer == "1":
    celsius = float(input("Enter your celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(fahrenheit)
elif answer == "2":
    fahrenheit = float(input("Enter your fahrenheit: "))
    celsius = (fahrenheit - 32)*1.8
    print(celsius)
else:
    print("Wrong input, please type 1 or 2")

answer = input("Choose \n1 to convert km -> miles, 2 to convert miles -> km: ")
if answer == "1":
    km = float(input("Enter km : "))
    miles = km / 1.609
    print(miles)
elif answer == "2":
    miles = float(input("Enter miles : "))
    km = miles * 1.609
    print(km)
else:
    print("Wrong input, please try again!")
