class Animals:
    name = "Animal"
    age = 8
    tail = True

    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name


class Cars:
    name = "Audi"
    type = "racecar"
    wheels = True
    doors = 2

    def print_name(self):
        print(self.name)


car = Cars()
car2 = Cars()
car3 = Cars()



car.print_name()
car

cat = Animals()
cat.name = "Barsik"
print(cat.name)

cat.print_name()
