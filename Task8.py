logs = [22, 25, "TIMEOUT", 28, 0, "ERROR", 30]

total_temperature = 0
valid_count = 0

for reading in logs:

    if reading == "TIMEOUT":
        continue

    if reading == 0:
        continue

    if reading == "ERROR":
        break

    total_temperature += reading
    valid_count += 1

average_temperature = total_temperature / valid_count

print("\nTask 8 - Dirty Data Integrator")
print("Sum of valid temperatures:", total_temperature)
print("Count of valid temperatures:", valid_count)
print(f"Average Temperature: {average_temperature:.2f}")