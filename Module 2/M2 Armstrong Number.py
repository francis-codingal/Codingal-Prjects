num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)

temp = num
total_sum = 0

while temp > 0:
    digit = temp % 10
    total_sum += digit ** num_digits
    temp //= 10

if total_sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
