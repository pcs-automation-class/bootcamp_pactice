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