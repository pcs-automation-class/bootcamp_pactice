class Animals:
    name = "Animal"
    age = 0
    tail = True

    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    def set_age(self):
        age = 0
        self.age = age

cat = Animals()
dog = Animals()
mice = Animals()

cat.print_name()
dog.print_name()
mice.print_name()

cat.name = "Barsik"
dog.name = "Rex"
mice.name = "Mickey"

cat.print_name()
dog.print_name()
mice.print_name()

#
#
#
#
#
#
#
#
#
#
# class Cat(Animals):
#     can_meow = True
#
#
#
# class Dog(Animals):
#     can_bark = True
#     self.name = "Dog"
#
#
#
# class LoginPage:
#     def __init__(self):
#         self.username = "//input[@name='name']"
#         self.password = "//input[@name='password']"
#
#     def type_in_field(self, field, text):
#         pass
#
#
# if __name__ == "__main__":
#     animal = Animals()
#     animal2 = Animals()
#     cat = Cat()
#     dog = Dog()
#
#     cat.set_name()
#
#
#     animal.print_name()
#     animal2.print_name()
#
#     animal.set_name("Dog")
#     animal2.set_name("Cat")
#
#     animal.print_name()
#     animal2.print_name()
#
#     pets = list()
#
#     pets.append(animal)
#     pets.append(animal2)
#
#     print(pets)
#
#     pets[0].print_name()
#     pets[1].print_name()
#
#     login_page = LoginPage()
#     login_page.type_in_field(login_page.username, "admin")
#
#
#     x = 0
#
#     def my_function():
#         y = x
#
#     x = y