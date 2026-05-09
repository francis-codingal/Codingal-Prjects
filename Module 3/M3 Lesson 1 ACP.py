def calculate_circumference(radius):
    pi_value = 3.14159
    return 2 * pi_value * radius

r = float(input("Enter the radius of the circle: "))

circumference = calculate_circumference(r)

print("The circumference of the circle is:", circumference)