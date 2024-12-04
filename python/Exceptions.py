
while True:
    try:
        try:
            answer1 = float(input("Input first number: "))
            answer2 = float(input("Input second number: "))
        except ValueError:
            print("You input not numeric value and it was set as 0")
            answer1 = 0
            answer2 = 0

        sign = input("Input sign: ")

        if sign == "+":
            print(answer1 + answer2)
        elif sign == "-":
            print(answer1 - answer2)
        elif sign == "/":
            print(answer1 / answer2)
        elif sign == "*":
            print(answer1 * answer2)
        else:
            print("Wrong operator")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print(e)

    print("Done")



# =============

# Setup()
# try:
#     run_code()
#     Teardown()
# except KeyboardInterrupt:
#     Teardown()
