word = input("Enter a string: ")

for char in word:
    if char == 'z':
        print("Letter z was identified")
        break
    else:
        print("Looking for z...")