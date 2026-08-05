shape = input("Enter shape (rectangle/triangle/square/circle): ").lower()

if shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    perimeter = 2 * (length + width)
    print(f"Perimeter of Rectangle: {perimeter}")

elif shape == "square":
    side = float(input("Enter side length: "))
    perimeter = 4 * side
    print(f"Perimeter of Square: {perimeter}")

elif shape == "triangle":
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))
    perimeter = a + b + c
    print(f"Perimeter of Triangle: {perimeter}")

elif shape == "circle":
    radius = float(input("Enter radius: "))
    perimeter = 2 * 3.14159 * radius
    print(f"Circumference of Circle: {perimeter}")

else:
    print("Invalid shape entered.")
