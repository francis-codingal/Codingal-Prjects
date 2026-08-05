num = int(input("Enter a decimal number: "))

if num == 0:
    binary = "0"
else:
    temp = num
    binary = ""
    while temp > 0:
        remainder = temp % 2
        binary = str(remainder) + binary
        temp //= 2

print(f"Binary of {num} is: {binary}")
