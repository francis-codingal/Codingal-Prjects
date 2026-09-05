from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def get_human_years(self) -> float:
        pass


class Dog(Animal):
    def get_human_years(self) -> float:
        return self.age * 7.0


class Cat(Animal):
    def get_human_years(self) -> float:
        return self.age * 6.0


dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 4)

print(f"{dog.name} ({dog.age} dog yrs) = {dog.get_human_years()} human yrs")
print(f"{cat.name} ({cat.age} cat yrs) = {cat.get_human_years()} human yrs")
