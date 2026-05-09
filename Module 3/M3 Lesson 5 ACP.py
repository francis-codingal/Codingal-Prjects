import math

angle = float(input("Enter the angle in degrees: "))

radians = math.radians(angle)

sine_val = math.sin(radians)
cosine_val = math.cos(radians)
tangent_val = math.tan(radians)

print(f"Trigonometric values for {angle}°:")
print(f"Sin: {sine_val}")
print(f"Cos: {cosine_val}")
print(f"Tan: {tangent_val}")