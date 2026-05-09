import string
import random

def generate_password(length):
    if length < 3:
        return "Password length must be at least 3 to include all character types."

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    all_characters = lower + upper + digits

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    password += random.choices(all_characters, k=length - 3)

    random.shuffle(password)

    return ''.join(password)

try:
    size = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(size))
except ValueError:
    print("Please enter a valid number for the length.")