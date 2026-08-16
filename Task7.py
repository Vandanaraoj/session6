print("\nTask 7 - Battery Charging Simulator")

battery = 0

while battery <= 100:
    battery += 5

    if battery in (20, 40, 60):
        print(f"Charging... Battery = {battery}%")

    elif battery == 80:
        pass
        print("Slow Charge Mode...")

    elif battery == 100:
        print("Fully Charged")
        break