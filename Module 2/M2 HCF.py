num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a, b = num1, num2
while b > 0:
    a, b = b, a % b

print(f"The HCF of {num1} and {num2} is {a}")
