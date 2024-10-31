# Conversion factors
MILES_TO_KM = 1.60934
KM_TO_MILES = 0.621371

print("Choose a conversion:")
print("1. Miles to Kilometers")
print("2. Kilometers to Miles")
print("3. Fahrenheit to Celsius")
print("4. Celsius to Fahrenheit")

choice = input("Enter 1, 2, 3, or 4: ")

if choice == '1':
    miles = float(input("Enter miles: "))
    km = miles * MILES_TO_KM
    print(f"{miles} miles is equal to {km:.2f} kilometers.")

elif choice == '2':
    km = float(input("Enter kilometers: "))
    miles = km * KM_TO_MILES
    print(f"{km} kilometers is equal to {miles:.2f} miles.")

elif choice == '3':
    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")

elif choice == '4':
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")

else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")

