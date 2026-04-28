start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

print(f"Prime numbers between {start} and {end}:")

for current_val in range(start, end + 1):
    if current_val > 1:
        for divisor in range(2, current_val):
            if (current_val % divisor) == 0:
                break
        else:
            print(current_val)