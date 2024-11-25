#a = 1
#print (type(a))

# def my_function():
#     print("This is my Function")
# #    my_function()


class Animals:
    name = "Animal"
    age = 0
    tail = True

    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

#Animals.tail = False

animal = Animals()
animal2 = Animals()
animal3 = Animals()

animal.print_name()
animal2.print_name()
animal3.print_name()

animal.set_name("Dog")
animal2.set_name("Cat")
animal3.set_name("Bird")


animal.print_name()
animal2.print_name()
animal3.print_name()

#list - this is also an object
pets = list()

pets.append(animal)
pets.append(animal2)
pets.append(animal3)

print(pets)
# [<__main__.Animals object at 0x10626bfd0>, <__main__.Animals object at 0x10626bfa0>, <__main__.Animals object at 0x10626bf70>]
pets[0].print_name()
pets[1].print_name()
pets[2].print_name()

# class LoginPage:
#    def __init__(self):
#        self.username = "//input[@name='username']"
#        self.password = "//input[@name='password']"
#
# login_page = LoginPage()
#
# login_page.username
# login_page.password
#
#     def type_in_field(self, field, text):
#         pass
#
#
# login_page.LoginPage()
# login_page.type_in_field(login_page.username, "Admin")


