height = int(input("Enter the triangle height: "))

for row in range(1, height + 1):
    spaces = height - row
    for s in range(spaces):
        print(" ", end="")
    
    for star in range(row):
        print("*", end="")
    print()