def print_until_letter(text, stop_char):
    for char in text:
        if char.lower() == stop_char.lower():
            print(f"Reached current letter '{char}'! Stopping execution.")
            break
        print(f"Current letter: {char}")

user_text = input("Enter a word or sentence: ")
target = input("Enter a letter to stop at: ")

print_until_letter(user_text, target)
