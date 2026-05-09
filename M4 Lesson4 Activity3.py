import array as arr

# create an array
array_num = arr.array('i', [10, 20, 30, 20, 40, 20, 50])
print("Original array: " + str(array_num))

# count number of occurrences
print("Number of occurrences of the number 20 in the said array: " + str(array_num.count(20)))

# reverse the array 
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))