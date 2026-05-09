class Parrot:

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

sky = Parrot("Sky", 5)
rio = Parrot("Rio", 8)

print("Sky is a {}".format(sky.species))
print("Rio is also a {}".format(rio.species))

print("{} is {} years old".format(sky.name, sky.age))
print("{} is {} years old".format(rio.name, rio.age))