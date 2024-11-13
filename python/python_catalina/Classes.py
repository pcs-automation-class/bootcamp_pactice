# Base Animal class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound."


# Dog class that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call the Animal class constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."


# Frenchie class that inherits from Dog
class Frenchie(Dog):
    def __init__(self, name, color):
        super().__init__(name, "French Bulldog")  # Call the Dog class constructor
        self.color = color

    def speak(self):
        return f"{self.name} snorts and barks in a cute way."

    def play(self):
        return f"{self.name} is running around playfully, making snorting noises!"


# Creating an object of the Frenchie class
my_frenchie = Frenchie("Bella", "Fawn")

# Accessing the attributes and methods
print(my_frenchie.name)  # Output: Bella
print(my_frenchie.breed)  # Output: French Bulldog
print(my_frenchie.color)  # Output: Fawn
print(my_frenchie.speak())  # Output: Bella snorts and barks in a cute way.
print(my_frenchie.play())  # Output: Bella is running around playfully, making snorting noises!


