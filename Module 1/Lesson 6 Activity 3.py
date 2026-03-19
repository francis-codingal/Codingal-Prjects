user_height = float(input("Enter your height in cm: "))
user_weight = float(input("Enter your weight in kg: "))

score = user_weight / (user_height / 100)**2

print("Your BMI is", score)

if score <= 18.4:
    print("Underweight status.")
elif score <= 24.9:
    print("Healthy weight status.")
elif score <= 29.9:
    print("Overweight status.")
elif score <= 34.9:
    print("Severely overweight status.")
elif score <= 39.9:
    print("Obese status.")
else:
    print("Severely obese status.")