rows = int(input("Enter the number of rows: "))

print("Half Pyramid Pattern:")

for current_row in range(rows):
    for column in range(current_row + 1):
        print("* ", end="")
    print()