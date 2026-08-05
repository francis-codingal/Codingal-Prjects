num = int(input("Enter a decimal number: "))

print("Choose target conversion:")
print("1. Binary")
print("2. Octal")
print("3. Hexadecimal")
print("4. All")

choice = input("Enter choice (1-4): ")

if choice == "1":
    print(f"Binary: {bin(num)[2:]}")
elif choice == "2":
    print(f"Octal: {oct(num)[2:]}")
elif choice == "3":
    print(f"Hexadecimal: {hex(num)[2:].upper()}")
elif choice == "4":
    print(f"Binary: {bin(num)[2:]}")
    print(f"Octal: {oct(num)[2:]}")
    print(f"Hexadecimal: {hex(num)[2:].upper()}")
else:
    print("Invalid choice.")
