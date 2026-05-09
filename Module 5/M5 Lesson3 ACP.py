class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_amount = super().fare()
        total_amount = base_amount + (0.10 * base_amount)
        return total_amount

school_bus = Bus("School Volvo", 12, 50)

print(f"Total {school_bus.name} fare is: INR {school_bus.fare()}")