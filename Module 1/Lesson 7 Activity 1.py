val = 100
if (type(val) is int):
    print("Correct: This is an integer")
else:
    print("Incorrect type")

val = 10.5
if (type(val) is not int):
    print("Correct: This is not an integer")
else:
    print("This is an integer")

first_num = 50
second_num = 50
if (first_num is second_num):
    print("Both variables share the same identity")

second_num = 100
if (first_num is not second_num):
    print("These variables now have different identities")