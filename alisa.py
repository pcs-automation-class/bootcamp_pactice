class Animals:
    name = "Animal"
    age = 8
    tail = True

    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name
class LoginPage:
    def __init__(self):
        self.username = "//input[@name='name']"
        self.password = "//input[@name='password']"

    