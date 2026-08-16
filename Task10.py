balance = 50

items = {
    "Soda": 15,
    "Chips": 10,
    "Candy": 5
}

print("\nTask 10 - Vending Machine")
print("Available Items:", items)
print("Starting Balance:", balance)

while True:

    if balance == 0:
        print("Balance is zero. Transaction ended.")
        break

    choice = input(
        "Enter item name or 'finished': "
    ).strip()

    if choice.lower() == "finished":
        print("Transaction finished.")
        break

    if choice not in items:
        print("Invalid item. Please try again.")
        continue

    item_price = items[choice]

    if item_price > balance:
        print(
            f"Insufficient balance for {choice}. "
            f"Your balance is ₹{balance}."
        )
        continue

    balance -= item_price

    print(
        f"{choice} purchased for ₹{item_price}."
    )
    print(f"Remaining balance: ₹{balance}")

    if balance == 0:
        print("Balance is zero. Transaction ended.")
        break

    # Refund section reserved for future implementation.
    pass

print("Thank you for using the vending machine.")