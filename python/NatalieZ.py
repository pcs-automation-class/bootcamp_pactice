from operator import truediv

print("Hello World!")
first_name = "Natalia"
last_name = "Z"
price = 23
price_2 = 20
age = 24
age_2 = 25
temperature = 18.5
temperature_2 = 20.5
print(first_name)
print (price + price_2)
print (age + age_2)
print (first_name, last_name)

print(type(str(age)))

answer = input("enter a number")
print(answer)

answer_1 = int(input("Enter first number: "))
answer_2 = int(input("Enter second number: "))
answer_3 = input("Enter operation [+, -, /, *]: ")

if answer_3 == "+":
    print(answer_1 + answer_2)

if answer_3 == "-":
    print(answer_1 - answer_2)

if answer_3 == "*":
    print(answer_1 * answer_2)

if answer_3 == "/":
    print(answer_1 / answer_2)

answer = input("choose \n1 to convert foot -> meter \n2 to convert meter -> foot: ")

#Convert foot to meter

if answer == "1":
    foot = float(input("enter foot: "))
    meter = foot / 3.281
    print(meter)
elif answer == "2":
    meter = float(input("enter meter: "))
    foot = meter * 3.281
    print(foot)
else:
    print("wrong input please try again")

# Convert C to F

answer = input("Choose \n1 to convert celsius -> fahrenheit, n2 to convert fahrenheit -> celsius: ")
if answer == "1":
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(fahrenheit)
elif answer == "2":
    fahrenheit = float(input("Enter fahrenheit: "))
    celsius = (fahrenheit - 32)*1.8
    print(celsius)
else:
    print("Wrong input, please type 1 or 2")


answer = input("Enter 1 to convert feet to meters or 2 to convert meters to feet: ")

if answer == "1":
    foot = float(input("Enter foot (0-1000): "))
    if foot < 0 or foot > 1000:
        print("Value out of range")
    else:
        meter = foot / 3.281
        print(f"{foot} feet is equal to {meter:.2f} meters")
elif answer == "2":
    meter = float(input("Enter meter (0-1000): "))
    if meter < 0 or meter > 1000:
        print("Value out of range")
    else:
        foot = meter * 3.281
        print(f"{meter} meters is equal to {foot:.2f} feet")
else:
    print("Wrong input, please try again")

a: bool = True
b: bool = False

#AND
True True = True
False True = False
True False = False
False False = False

# OR
True True = True
False True = True
True False = True
False False = False

#NOT
not True = False
not False = True