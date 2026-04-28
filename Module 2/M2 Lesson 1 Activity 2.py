gb_used = int(input("How many GBs did you use this month? "))

if gb_used <= 10:
    bill = gb_used * 5  # Cheap tier
    tax = 2
elif gb_used <= 30:
    bill = 50 + ((gb_used - 10) * 10)  # Mid tier
    tax = 5
else:
    bill = 50 + 200 + ((gb_used - 30) * 20)  # "Unlimited" (but expensive) tier
    tax = 10

print(f"Total Phone Bill: ${bill + tax}")