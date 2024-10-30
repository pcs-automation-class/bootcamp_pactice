#convert farenheit to celcius and vs
answer1 = (input("Enter \n1 to convert cel to far \n2 for far to cel: "))
if answer1 == "1":
    far = float(input("Enter your far: "))
    cel = (far - 32) * (5/9)
    print(cel)
elif answer1 == "2":
    cel= float(input("Enter your cel: "))
    far = cel * (9/5) + 32
    print(far)
else: print("Wrong input.")

print("Done!")
