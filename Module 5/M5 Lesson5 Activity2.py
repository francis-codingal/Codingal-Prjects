from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I walk on two legs")

class Panther(Animal):

    def move(self):
        print("I move silently in the shadows")

class Wolf(Animal):

    def move(self):
        print("I run with the pack")

class Dog(Animal):

    def move(self):
        print("I run on four legs")

class Lion(Animal):

    def move(self):
        print("I prowl through the grass")

class Elephant(Animal):

    def move(self):
        print("I walk with heavy steps")

person = Human()
person.move()

bagheera = Panther()
bagheera.move()

ghost = Wolf()
ghost.move()

husky = Dog()
husky.move()

simba = Lion()
simba.move()

hathi = Elephant()
hathi.move()