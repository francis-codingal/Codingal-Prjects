print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("Maths :"))
english = int(input("English :"))
science = int(input("Science :"))
history = int(input("History :"))

total_marks = math + english + science + history
print("Total marks obtained =", total_marks)

percentage = (total_marks / 400) * 100

print(end="Percentage Mark = ")
print(percentage)