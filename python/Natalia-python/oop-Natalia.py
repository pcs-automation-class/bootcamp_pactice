
class Drinks:
    def __init__(self):
        self.name = "drink"
        self.taste = "sweet"
        self.type = "cold"
        self.size = "16 oz"

    def print_name(self):
        print(self.name)

drink = Drinks()
drink.print_name()

drink = Drinks()
coffee = Drinks()
tea = Drinks()

drink.print_name()
coffee.print_name()
tea.print_name()

drink.name = "milk"
coffee.name = "decaf"
tea.name = "matcha"

drink.print_name()
coffee.print_name()
tea.print_name()
