text = input("Enter a word: ")
target = input("Enter a character to find: ")

index = 0
occurrences = 0

while index < len(text):
    if text[index] == target:
        occurrences += 1
    index += 1

print(f"The character '{target}' appeared {occurrences} times.")