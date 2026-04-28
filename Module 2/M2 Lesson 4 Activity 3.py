value = int(input("Enter an integer: "))

original = value
length = 0
temp_val = value

while temp_val > 0: 
    length += 1
    temp_val //= 10

if length >= 4:
    midpoint = length // 2
    position = 0
    
    while value > 0:
        digit = value % 10
        if position == midpoint:
            first_mid = digit
        elif position == (midpoint - 1): 
            second_mid = digit
        value //= 10
        position += 1
        
    result = first_mid * second_mid
    print(f"\nProduct of middle digits ({first_mid} * {second_mid}) = {result}")

else:
    print("\nThe number must have at least 4 digits!")