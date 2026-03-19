cost_price = float(input(" Please Enter the Actual Product Price: "))
selling_price = float(input(" Please Enter the Sales Amount: "))

if (selling_price > cost_price):
    profit = selling_price - cost_price
    print("Total Profit = {0}".format(profit))
else:
    print("No Profit!!!")