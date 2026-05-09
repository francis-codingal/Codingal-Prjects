def total_calc(bill_amount, tip_perc=15):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Total amount to pay: ${total}")

total_calc(85)
total_calc(200, 10)