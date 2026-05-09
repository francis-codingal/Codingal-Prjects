class Dog:
    # Class variable
    animal = "Mammal"

    def __init__(self, breed, colour):
        # Instance variables
        self.breed = breed
        self.colour = colour

# Creating two different objects for different breeds
golden_retriever = Dog("Golden Retriever", "Golden")
husky = Dog("Siberian Husky", "Grey and White")

# Displaying details for the first breed
print("Details of Dog 1:")
print("Animal Type:", Dog.animal)
print("Breed:", golden_retriever.breed)
print("Colour:", golden_retriever.colour)

print("-" * 20)

# Displaying details for the second breed
print("Details of Dog 2:")
print("Animal Type:", Dog.animal)
print("Breed:", husky.breed)
print("Colour:", husky.colour)