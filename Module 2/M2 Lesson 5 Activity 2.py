total_steps = int(input("Enter the number of rows: "))
current_digit = 1

print("Floyd's Triangle Result:")

for row_idx in range(1, total_steps + 1):
    for col_idx in range(1, row_idx + 1):
        print(current_digit, end=' ')
        current_digit += 1
    print()