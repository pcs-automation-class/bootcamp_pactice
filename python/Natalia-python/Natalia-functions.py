def display_invoice(username, amount, due_date):
    print(f"Hello {username}!")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Natalia", 57.75, "01/01")


def create_name(first, last):  # Removed quotes and added a colon
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Mary", "Jane")  # Fixed the function name typo

print(full_name)
