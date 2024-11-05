#converter
def convert(choice):
        if choice == 1:
                n = float(input("Enter your °F: "))
                result = round(((n - 32) * 5 / 9), 1)
                print(f"{n}°F is equal to {result}°C")

        elif choice == 2:
                n = float(input("Enter your °C: "))
                result = round((n * 9 / 5 + 32), 1)
                print(f"{n}°C is equal to {result}°F")

        elif choice == 3:
                n = float(input("Enter your mi: "))
                result = round(n * 1.60934, 2)
                print(f"{n}mi is equal to {result}km")

        elif choice == 4:
                n = float(input("Enter your km: "))
                result = round(n / 1.60934, 2)
                print(f"{n}km is equal to {result}mi")

        else:
                print("Enter a number from 1 to 4")

def print_line():
        print("-" * 30)

while True:
        print("What to convert?")
        print("1. °F to °C")
        print("2. °C to °F")
        print("3. mi to km")
        print("4. km to mi")
        choice = int(input("Enter your choice: "))
        print_line()
        n = result = 0
        convert(choice)
        print_line()
        answer = input("Do you want to continue? (y/n) : ")
        if answer.lower() == "n":
                break