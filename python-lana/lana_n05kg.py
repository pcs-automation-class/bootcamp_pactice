#convert kilometers to miles

answer1 = (input("Enter \n1 to convert kg to pounds \n2 for pounds to kg: "))
if answer1 == "1":
    kg = float(input("Enter your kg: "))
    pound = kg * 2.205
    print(pound)
elif answer1 == "2":
    pound= float(input("Enter your pounds: "))
    kg = pound / 2.205
    print(kg)
else: print("Wrong input.")

print("Done!")

#pound/2.205 = kg