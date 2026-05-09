is_valid = False

while not is_valid:
    try:
        age = int(input("Enter your age: "))
        
        if age < 0:
            print("Age cannot be negative. Please try again.")
            continue
            
        if age % 2 == 0:
            print(f"The age {age} is an Even number.")
        else:
            print(f"The age {age} is an Odd number.")
            
        is_valid = True
        
    except ValueError:
        print("Value Error: Please enter a valid whole number (no decimals, letters, or symbols).")

print("Verification complete.")