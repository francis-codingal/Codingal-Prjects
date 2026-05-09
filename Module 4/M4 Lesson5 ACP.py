limit = int(input("Enter a number: "))

# List of odd numbers under the input value
odds = [x for x in range(limit) if x % 2 != 0]

# List of even numbers under the input value
evens = [x for x in range(limit) if x % 2 == 0]

print("Odd numbers list:", odds)
print("Even numbers list:", evens)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Capitalize the first letter of every element
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("Updated fruits:", capitalized_fruits)