
def stock_tracker():
    # 1. Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 370
    }
    
    portfolio = {}
    total_value = 0

    print("--- Stock Portfolio Tracker ---")
    print(f"Available stocks: {', '.join(stock_prices.keys())}\n")

    # 2. User Input
    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper()
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                quantity = int(input(f"Enter quantity for {symbol}: "))
                portfolio[symbol] = quantity
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Stock not found in database. Please try AAPL, TSLA, GOOGL, or MSFT.")

    # 3. Calculation
    print("\n--- Portfolio Summary ---")
    summary_text = "Stock | Quantity | Price | Subtotal\n" + "-"*35 + "\n"
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        subtotal = qty * price
        total_value += subtotal
        line = f"{stock:5} | {qty:8} | ${price:4} | ${subtotal:8}\n"
        summary_text += line
        print(line.strip())

    summary_text += f"-"*35 + f"\nTotal Investment Value: ${total_value}"
    print(f"\nTotal Investment Value: ${total_value}")

    # 4. Optional: Save to File
    save = input("\nSave results to portfolio.txt? (y/n): ").lower()
    if save == 'y':
        with open("portfolio.txt", "w") as f:
            f.write(summary_text)
        print("File saved successfully!")

if __name__ == "__main__":
    stock_tracker()
