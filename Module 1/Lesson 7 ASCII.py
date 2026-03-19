print("ASCII Value Checker")
print("-" * 30)

user_input = input("Enter a single character: ")

if len(user_input) == 1:
    code = ord(user_input)
    
    print(f"\nCharacter: '{user_input}'")
    print(f"ASCII Value: {code}")
    
    print("\nCharacter Type: ", end="")
    if 65 <= code <= 90:
        print("Uppercase Letter")
    elif 97 <= code <= 122:
        print("Lowercase Letter")
    elif 48 <= code <= 57:
        print("Digit")
    elif code == 32:
        print("Space")
    else:
        print("Special Character")
else:
    print("\nError: Please enter exactly ONE character!")