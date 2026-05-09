# A. Sets for colors
set_a1 = {'blue', 'green'}
set_a2 = {'blue', 'yellow'}

sym_diff_a = set_a1.symmetric_difference(set_a2)

print("Symmetric Difference (A):")
print(f"Set 1: {set_a1}")
print(f"Set 2: {set_a2}")
print(f"Result: {sym_diff_a}")

print("-" * 30)

# B. Sets for numbers
set_b1 = {1, 2, 3, 4, 5}
set_b2 = {1, 5, 6, 7, 8, 9}

sym_diff_b = set_b1.symmetric_difference(set_b2)

print("Symmetric Difference (B):")
print(f"Set 1: {set_b1}")
print(f"Set 2: {set_b2}")
print(f"Result: {sym_diff_b}")