def square(value):
    return value * value

def check_divisibility(value):
    if value % 5 == 0:
        return square(value)
    else:
        return False

print(check_divisibility(10))
print(check_divisibility(7))