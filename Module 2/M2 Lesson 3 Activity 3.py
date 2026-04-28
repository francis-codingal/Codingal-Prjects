val = int(input("Enter an integer: "))

total = 0
remainder = val

while remainder > 0:
    unit = remainder % 10
    total += unit ** 4
    remainder //= 10

if val == total:
    print(val, "matches the power sum criteria")
else:
    print(val, "does not match the power sum criteria")