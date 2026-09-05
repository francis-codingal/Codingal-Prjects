class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width


rect = Rectangle(5.0, 4.0)
print("Area:", rect.calculate_area())
