num = int(input("Enter a number: "))
temp = num
total_sum = 0

while temp > 0:
    digit = temp % 10
    
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
        
    total_sum += factorial
    temp //= 10

if total_sum == num:
    print(f"{num} is a Strong number")
else:
    print(f"{num} is not a Strong number")
