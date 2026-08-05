num = int(input("Enter a number: "))
temp = num
reverse_num = 0

while temp > 0:
    digit = temp % 10
    reverse_num = (reverse_num * 10) + digit
    temp //= 10

if num == reverse_num:
    print(f"{num} is a Palindrome number")
else:
    print(f"{num} is not a Palindrome number")
