num_str = input("Enter a number: ")

if len(num_str) <= 2:
    print("Number must have at least 3 digits to have middle digits")
else:
    mid_str = num_str[1:-1]
    product = 1
    for digit in mid_str:
        product *= int(digit)
    print(f"Product of middle digits ({mid_str}) is: {product}")
