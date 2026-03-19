score_x = int(input("Enter first score: "))
score_y = int(input("Enter second score: "))
score_z = int(input("Enter third score: "))

result_avg = (score_x + score_y + score_z) / 3
print(f"Average: {result_avg}")

if result_avg > score_x and result_avg > score_y and result_avg > score_z:
    print(f"{result_avg} is higher than {score_x}, {score_y}, and {score_z}")
elif result_avg > score_x and result_avg > score_y:
    print(f"{result_avg} is higher than {score_x} and {score_y}")
elif result_avg > score_x and result_avg > score_z:
    print(f"{result_avg} is higher than {score_x} and {score_z}")
elif result_avg > score_y and result_avg > score_z:
    print(f"{result_avg} is higher than {score_y} and {score_z}")
elif result_avg > score_x:
    print(f"{result_avg} is just higher than {score_x}")
elif result_avg > score_y:
    print(f"{result_avg} is just higher than {score_y}")
elif result_avg > score_z:
    print(f"{result_avg} is just higher than {score_z}")
else:
    print("The average is not higher than any individual score.")