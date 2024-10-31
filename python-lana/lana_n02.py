answer1 = int(input("Enter first number: "))
answer2 = int(input("Enter second number: "))

print(answer1 + answer2)

#summy = answer1 + answer2
#subby = answer1 - answer2
#divvy = answer1 / answer2
#mully = answer1 * answer2
#print(summy, subby, divvy, mully)

answer3 = input("Enter a symbol of the operation [+, -, /, * }")
if answer3 == "+":
    print(answer1 + answer2)
elif answer3 == "-":
    print(answer1 - answer2)
elif answer3 == "*":
    print(answer1 * answer2)
elif answer3 == "/":
    print(answer1 / answer2)
else: print("Wrong input.")

print("Done!")







