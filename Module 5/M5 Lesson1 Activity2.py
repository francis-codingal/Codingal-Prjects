class Vehicle:

    def __init__(self, top_speed, fuel_efficiency):

        self.top_speed = top_speed
        self.fuel_efficiency = fuel_efficiency

roxx = Vehicle(160, 15)

print("Roxx Top Speed:", roxx.top_speed)
print("Roxx Fuel Efficiency:", roxx.fuel_efficiency)