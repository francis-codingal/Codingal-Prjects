print("Enter a Number (Numerator): ")
numerator = int(input())
print("Enter a Number (Denominator): ")
denominator = int(input())

if numerator % denominator == 0:
    print("\n" + str(numerator) + " is divisible by " + str(denominator))
else:
    print("\n" + str(numerator) + " is not divisible by " + str(denominator))