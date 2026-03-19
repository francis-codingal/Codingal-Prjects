brand = "Apple"
quantity = 25
in_stock = False
price = 99.99

print("Brand :", brand)
print("Data Type of Brand is", type(brand))

print("Quantity :", quantity)
print("Data Type of Quantity is", type(quantity))

print("In Stock :", in_stock)
print("Data Type of In Stock is", type(in_stock))

print("Price :", price)
print("Data Type of Price is", type(price))

print("\nAfter Type Casting....")

quantity = str(quantity)
print(quantity)
print("Data Type of Quantity is", type(quantity))

price = int(price)
print(price)
print("Data Type of Price is", type(price))