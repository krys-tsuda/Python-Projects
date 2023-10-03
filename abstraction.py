

from abc import ABC, abstractmethod

# parent class
class Animal(ABC):
    def __init__(self, name):
        self.name = name
   
    # abstract method
    @abstractmethod
    def make_sound(self):
        pass

    # regular method
    def display_info(self):
        print(f"This is {self.name}.")


# child class
class Dog(Animal):
    def make_sound(self):
        return "Bark!"


dog = Dog("Ruca")
dog.display_info()
print(f"{dog.name} says: {dog.make_sound()}")
