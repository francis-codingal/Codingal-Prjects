import random

active = True
target_digit = str(random.randint(10, 50))

print("I am thinking of a number between 10 and 50.")
print("The game continues until you identify the secret value!")

while active:
    attempt = input("Enter your guess: ")
    
    if target_digit == attempt:
        print("Fantastic! You've guessed correctly.")
        print("The secret value was", target_digit)
        active = False
    
    else:
        print("That is incorrect. Keep trying!")