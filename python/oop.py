class Animals:
    name = ""
    age = 0
    tail = True

    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    def set_age(self):
        age = 0
        self.age = age


class Cat(Animals):
    def __init__(self):
        self.can_meow = True
        self.name = "Kuzya"


class WhiteCat(Cat):
    def __init__(self, color: str = "White"):
        # super().__init__()
        self.color = color
        self.name = "Cat"

    def get_color(self) -> str:
        return self.color

    def print_name(self):
        print(f"Name: {self.name}")


# my_cat = WhiteCat()
# cat = WhiteCat()
# my_cat.print_name()
# cat.set_name("Cat")
# cat.print_name()

first = 1
second = "w"
result = 0

try:
    result = first / second
except ZeroDivisionError:
    print("Do not divide to zero!")
except TypeError:
    print("Wrong value")
# except Exception as e:
#     print(e)


print(result)
