import numpy as np

arr = np.linspace(0, 9, 10)

new_arr = np.where(arr % 2 != 0, -1, arr)

arr_2d = arr.reshape(2, 5)

even_sum = 0
for element in arr:
    if element % 2 == 0:
        even_sum += element

print("Original 1D Array:")
print(arr)
print("\nModified Array (Odd numbers replaced with -1):")
print(new_arr)
print("\nConverted 2D Array (2 rows):")
print(arr_2d)
print("\nSum of all even elements:")
print(even_sum)
