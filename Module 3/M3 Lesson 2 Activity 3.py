def summation(n):
    """this is a recursive function to find the sum of integers up to n"""

    if n == 0:
        return 0
    else:
        return n + summation(n - 1)

print(summation.__doc__)
print("the sum up to 0:", summation(0))
print("the sum up to 1:", summation(1))
print("the sum up to 3:", summation(3))
print("the sum up to 6:", summation(6))
print("the sum up to 10:", summation(10))