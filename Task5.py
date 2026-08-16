print("\nTask 5 - Command-Line Interface")

while True:
    command = input(
        "Enter command (status/reset/exit): "
    ).lower()

    match command:
        case "status":
            print("System Status: ONLINE")

        case "reset":
            print("System has been reset.")

        case "exit":
            print("Exiting system...")
            break

        case _:
            print("Invalid command. Please try again.")