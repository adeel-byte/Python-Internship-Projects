# Dictionary of stock prices
stock_prices = {
    "apple": 180,
    "tesla": 250,
    "google": 140,
    "amazon": 130,
    "microsoft": 320
}

total_investment = 0

print("Stock Portfolio Tracker\n")

while True:
    stock = input("Enter stock name (or 'end' to finish): ").lower()

    if stock == "end":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        price = stock_prices[stock]

        investment = price * quantity
        total_investment += investment

        print(f"Investment in {stock}: ${investment}\n")

    else:
        print("Stock not found in database.\n")

print("Total Investment Value: $", total_investment)