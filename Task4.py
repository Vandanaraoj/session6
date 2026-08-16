import random

random_numbers = [random.randint(1, 50) for _ in range(20)]

print("\nTask 4 - Smart Search Optimizer")
print("Generated List:", random_numbers)

target_id = int(input("Enter a number to search: "))

found = False

for index, value in enumerate(random_numbers):
    print(f"Analyzing index {index}...")

    if value == target_id:
        print(f"Target {target_id} found at index {index}.")
        found = True
        break

if found:
    if index < len(random_numbers) - 1:
        print("Search was efficient - stopped before the end.")
    else:
        print("Target found at the last index.")
else:
    print("Search was exhaustive - every element was checked.")