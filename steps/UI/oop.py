class Animals:
    name = "Animal"
    age = 0
    tail = True

    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name


animal = Animals()
animal2 = Animals()

animal.print_name()
animal2.print_name()

animal.set_name("Dog")
animal2.set_name("Cat")

animal.print_name()
animal2.print_name()

pets = list()

pets.append(animal)
pets.append(animal2)

print(pets)

pets[0].print_name()
pets[1].print_name()


class LoginPage:
    def __init__(self):
        self.username = "//input[@name='name']"
        self.password = "//input[@name='password']"

    def type_in_field(self, field, text):
        pass


login_page = LoginPage()
login_page.type_in_field(login_page.username, "admin")
