#convert kilometers to miles

answer1 = (input("Hello there \n1 Enter km to convert km to miles \n2 Enter miles for miles to km: "))
if answer1 == "1":
    km = float(input("Enter your km (1 - 1000) : "))
    if km <= 0 or km > 1000:
        print("Value is out of range")
    else:
        miles = km / 1.609
        print(miles)
elif answer1 == "2":
    miles= float(input("Enter your miles (1 - 1000) : "))
    if miles <= 0 or miles > 1000:
        print("Value is out of range")
    else:
        km = miles * 1.609
        print(km)
else: print("Wrong input. Please try again")

print("Done!")
#boundary testing: (1 to 1000). We test -1, 0, 1, 500, 999, 1000, 1001
