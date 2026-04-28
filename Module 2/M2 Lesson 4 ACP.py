decimal_val = int(input("Enter a decimal number: "))

binary_str = ""
temp_num = decimal_val

if temp_num == 0:
    binary_str = "0"

while temp_num > 0:
    remainder = temp_num % 2
    binary_str = str(remainder) + binary_str
    temp_num //= 2

print(f"The binary equivalent of {decimal_val} is: {binary_str}")