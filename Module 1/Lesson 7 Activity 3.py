print("Enter Marks Obtained in 5 Subjects: ")

score1 = int(input())
score2 = int(input())
score3 = int(input())
score4 = int(input())
score5 = int(input())

total = score1 + score2 + score3 + score4 + score5
average_mark = total / 5

if average_mark >= 91 and average_mark <= 100:
    print("Your Grade is A1")
elif average_mark >= 81 and average_mark < 91:
    print("Your Grade is A2")
elif average_mark >= 71 and average_mark < 81:
    print("Your Grade is B1")
elif average_mark >= 61 and average_mark < 71:
    print("Your Grade is B2")
elif average_mark >= 51 and average_mark < 61:
    print("Your Grade is C1")
elif average_mark >= 41 and average_mark < 51:
    print("Your Grade is C2")
elif average_mark >= 33 and average_mark < 41:
    print("Your Grade is D")
elif average_mark >= 21 and average_mark < 33:
    print("Your Grade is E1")
elif average_mark >= 0 and average_mark < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")