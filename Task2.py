
prices = [120.5, 118.2, 122.0, 115.5, 125.0]
starting_price = prices[0]

print("\nTask 2 - Financial Threshold Monitor")

for index, price in enumerate(prices):
    percentage_change = (
        (price - starting_price) / starting_price
    ) * 100

    print(
        f"Index {index}: Price = {price}, "
        f"Change = {percentage_change:.2f}%"
    )

    if percentage_change < -5:
        print(f"SELL ALERT - Index {index}")