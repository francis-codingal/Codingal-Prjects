def exponent(x, y):
    return x ** y

def floor_division(x, y):
    return x // y

def modulus(x, y):
    return x % y

def average(x, y):
    return (x + y) / 2

print("Select a math operation:")
print("1. Power")
print("2. Floor Division")
print("3. Modulo")
print("4. Average")

selection = input("Enter selection (1/ 2/ 3/ 4): ")

val_1 = float(input("Enter the first value: "))
val_2 = float(input("Enter the second value: "))

if selection == '1':
    print(val_1, "to the power of", val_2, "=", exponent(val_1, val_2))

elif selection == '2':
    print(val_1, "floor divided by", val_2, "=", floor_division(val_1, val_2))

elif selection == '3':
    print("The remainder of", val_1, "divided by", val_2, "is", modulus(val_1, val_2))

elif selection == '4':
    print("The average of", val_1, "and", val_2, "is", average(val_1, val_2))

else:
    print("Invalid selection")