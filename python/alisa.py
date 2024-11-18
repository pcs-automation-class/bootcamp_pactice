# # price = "18"
# # price_2 = "25"
# # print(int(price) + int(price_2))
# # print(int(price) - int(price_2))
# # print(type(int(price) * int(price_2)))
#
# answer = input("Enter first numer: ")
# answer_2 = input("Enter second numer: ")
# # print(int(answer) + int(price_2))
# # print(int(answer) + int(answer_2))
#
# answer_3 = input("Enter operation [+, -, *, /]: ")
#
# if answer_3 == "+":
#     print(int(answer) + int(answer_2))
#
# elif answer_3 == "-":
#     print(int(answer) - int(answer_2))
#
# elif answer_3 == "*":
#     print(int(answer) * int(answer_2))
#
# elif answer_3 == "/":
#     print(int(answer) / int(answer_2))
#
# else:
#     print('Wrong inpput')
#
# print("Done.")

answer = input("Choose: \n1 convert miles to km. \n2 convert km to miles. \nYour choice: ")

if answer == "2":
    km = float(input("Enter km: "))
    miles = km / 1.609
    print(f"{miles} miles")
elif answer == "1":
    miles = float(input("Enter miles: "))
    km = miles * 1.609
    print(f"{km} km")
else:
    print("Wrong input.")

