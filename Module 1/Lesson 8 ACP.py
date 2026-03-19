a = 10
b = 20
c = 30

print(f"Before: a={a}, b={b}, c={c}")

temp = a
a = c
c = b
b = temp

print(f"After:  a={a}, b={b}, c={c}")