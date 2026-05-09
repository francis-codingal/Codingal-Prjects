class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

# Changed the object name and the arguments
City_Express = Bus("City Express", 120, 8)

print("Vehicle Name:", City_Express.name, "Speed:", City_Express.max_speed, "Mileage:", City_Express.mileage)