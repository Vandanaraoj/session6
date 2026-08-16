print("\nTask 6 - 5x5 Grid Coordinates")

for row in range(5):
    for column in range(5):

        if row == 2 and column == 2:
            continue

        print(f"({row}, {column})")