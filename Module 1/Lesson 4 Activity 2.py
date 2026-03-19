withdrawal_amount = int(input("Please Enter Amount for Withdraw :"))

hundreds = withdrawal_amount // 100
fifties = (withdrawal_amount % 100) // 50
tens = ((withdrawal_amount % 100) % 50) // 10

print("notes of 100 rupee", hundreds)
print("notes of 50 rupee", fifties)
print("notes of 10 rupee", tens)