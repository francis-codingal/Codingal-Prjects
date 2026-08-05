def find_number(numbers, target):
    for num in numbers:
        if num == target:
            print(f"Found {target}! Stopping search.")
            break
        print(f"Checking {num}...")

num_list = [10, 25, 40, 55, 70, 85]
search_val = int(input("Enter number to search (e.g. 55): "))

find_number(num_list, search_val)
