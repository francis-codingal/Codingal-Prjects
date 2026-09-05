class Animal:
    pass


class Dog(Animal):
    pass


class Cat:
    pass


print(issubclass(Dog, Animal))
print(issubclass(Cat, Animal))
