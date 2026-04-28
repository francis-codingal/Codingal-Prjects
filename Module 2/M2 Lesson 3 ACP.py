user_input = input("Enter a number: ").strip()
digit_count = len(user_input.strip('-').replace('.', ''))

print(f"Total digits: {digit_count}")