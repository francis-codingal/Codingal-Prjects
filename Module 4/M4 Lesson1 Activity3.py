L = [12, 45, 2, 67, 31, 8, 99, 54]
print("Original List :", L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

L.sort()

print("Smallest element is:", L[0])
print("Largest element is:", L[-1])