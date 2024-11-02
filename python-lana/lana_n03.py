#convert kilometers to miles

answer1 = (input("Enter \n1 to convert km to miles \n2 for miles to km: "))
if answer1 == "1":
    km = float(input("Enter your km: "))
    miles = km * 1.609
    print(miles)
elif answer1 == "2":
    miles= float(input("Enter your miles: "))
    km = miles/1.609
    print(km)
else: print("Wrong input.")

print("Done!")