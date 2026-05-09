s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3, "\n")

list1 = [5, 10, 15, 20]
list2 = [50, 60, 70, 80]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

stocks = ['apple', 'microsoft', 'nvidia']
prices = [180, 420, 900]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))