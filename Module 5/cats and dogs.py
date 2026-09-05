from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"


animals = [Dog(), Cat()]

for animal in animals:
    print(type(animal).__name__, "says:", animal.speak())
