def calculate_change(bill_amount, paid_amount):
    return paid_amount - bill_amount

bill = 2.50
paid = 4.00

change_due = calculate_change(bill, paid)

print(f"Total Bill: ${bill}")
print(f"Amount Paid: ${paid}")
print(f"Change to return: ${change_due}")