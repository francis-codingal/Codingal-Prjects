size = int(input("Enter the total height of the diamond: "))

if size % 2 == 0:
    mid_point = size // 2
else:
    mid_point = (size // 2) + 1

gap = mid_point - 1

for r in range(1, mid_point + 1):
    for s in range(1, gap + 1):
        print(end=" ")
    gap -= 1
    val = 1
    for c in range(2 * r - 1):
        print(end=str(val))
        val += 1
    print()

gap = 1
for r in range(1, mid_point):
    for s in range(1, gap + 1):
        print(end=" ")
    gap += 1
    val = 1
    for c in range(1, 2 * (mid_point - r)):
        print(end=str(val))
        val += 1
    print()