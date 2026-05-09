test_dict = {'Apple' : 5, 'Banana' : 3, 'Cherry' : 5, 'Date' : 5, 'Elderberry' : 2}

print("The original dictionary : " + str(test_dict))

K = 5

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("Frequency of K is : " + str(res))