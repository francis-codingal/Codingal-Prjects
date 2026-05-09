import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

try:
    user_radius = float(input("Enter the radius of the circle: "))
    
    my_circle = Circle(user_radius)
    
    print("Area of the circle: %.2f" % my_circle.area())
    print("Perimeter of the circle: %.2f" % my_circle.perimeter())

except ValueError:
    print("Invalid input! Please enter a numeric value for the radius.")