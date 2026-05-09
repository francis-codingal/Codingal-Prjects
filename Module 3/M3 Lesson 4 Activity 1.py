try:
    value = int(input("Enter your age: "))
    print("Your age is", value)
except ValueError as error:
    print("Input Error:", error)