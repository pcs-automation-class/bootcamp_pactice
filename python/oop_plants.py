class Plants:
    def __init__(self, name="Plant", age=0, leaves=True):
        self.name = name
        self.age = age
        self.leaves = leaves

    def print_info(self):
        print(f"Name: {self.name}. Age: {self.age} years. Has leaves: {self.leaves}")

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


# Создание объектов с разными параметрами
plant = Plants(name="Oak", age=5)
plant2 = Plants(name="Maple", age=3)
cactus = Plants(name="Cactus", age=10, leaves=False)

# Печать информации о каждом объекте
plant.print_info()
plant2.print_info()
cactus.print_info()

# Пример изменения возраста для объекта
plant.set_age(6)
plant.print_info()


class LoginPage:
    def __init__(self):
        self.username = "//input[@name='name']"
        self.password = "//input[@name='password']"

    def type_in_field(self, field, text):
        pass


login_page = LoginPage()
login_page.type_in_field(login_page.username, "admin")