

from abc import ABC, abstractmethod

# parent class
class Animal:
    def __init__(self, name):
        self.name = name

    # abstract method
    def make_sound(self):
        pass

    # regular method
    def display_info(self):
        print(f"This is {self.name}.")


# child class
class Dog(Animal):
    def make_sound(self):
        return "Bark!"


# creating object of Dog class

dog = Dog("Ruca")

# method from parent class
dog.display_info()

# method from child class
print(f"{dog.name} says: {dog.make_sound()}")
