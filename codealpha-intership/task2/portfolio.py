# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

from datetime import datetime


# -----------------------------
# Stock Price Database
# -----------------------------
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 175.00,
    "MSFT": 420.00,
    "AMZN": 190.00
}


# -----------------------------
# Display Available Stocks
# -----------------------------
def display_stocks():
    print("\nAvailable Stocks")
    print("-" * 35)

    for stock, price in STOCK_PRICES.items():
        print(f"{stock:<10} ${price:>10.2f}")

    print("-" * 35)


# -----------------------------
# Get Valid Quantity
# -----------------------------
def get_quantity(stock):
    while True:
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            return quantity

        except ValueError:
            print("Please enter a valid whole number.")


# -----------------------------
# Add Stock to Portfolio
# -----------------------------
def add_stock(portfolio):
    stock = input("\nEnter stock symbol: ").upper().strip()

    if stock not in STOCK_PRICES:
        print("Stock not available in the database.")
        return

    quantity = get_quantity(stock)

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    print(f"Added {quantity} shares of {stock}.")


# -----------------------------
# Display Portfolio
# -----------------------------
def display_portfolio(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    print("\n" + "=" * 65)
    print("                 YOUR STOCK PORTFOLIO")
    print("=" * 65)

    print(
        f"{'Stock':<12}"
        f"{'Quantity':<12}"
        f"{'Price':<15}"
        f"{'Investment':<15}"
    )

    print("-" * 65)

    total_investment = 0

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        investment = quantity * price
        total_investment += investment

        print(
            f"{stock:<12}"
            f"{quantity:<12}"
            f"${price:<14.2f}"
            f"${investment:<14.2f}"
        )

    print("-" * 65)
    print(f"{'TOTAL INVESTMENT':<39} ${total_investment:.2f}")
    print("=" * 65)


# -----------------------------
# Calculate Total Investment
# -----------------------------
def calculate_total(portfolio):
    total = 0

    for stock, quantity in portfolio.items():
        total += quantity * STOCK_PRICES[stock]

    return total


# -----------------------------
# Save Portfolio to File
# -----------------------------
def save_portfolio(portfolio):
    if not portfolio:
        print("\nNothing to save. Your portfolio is empty.")
        return

    filename = "portfolio_report.txt"
    total = calculate_total(portfolio)

    with open(filename, "w") as file:
        file.write("CODEALPHA STOCK PORTFOLIO REPORT\n")
        file.write("=" * 45 + "\n")
        file.write(
            f"Generated: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.write("=" * 45 + "\n\n")

        file.write(
            f"{'Stock':<12}"
            f"{'Quantity':<12}"
            f"{'Price':<12}"
            f"{'Investment':<15}\n"
        )

        file.write("-" * 50 + "\n")

        for stock, quantity in portfolio.items():
            price = STOCK_PRICES[stock]
            investment = quantity * price

            file.write(
                f"{stock:<12}"
                f"{quantity:<12}"
                f"${price:<11.2f}"
                f"${investment:<14.2f}\n"
            )

        file.write("-" * 50 + "\n")
        file.write(f"Total Investment: ${total:.2f}\n")

    print(f"\nPortfolio successfully saved to '{filename}'.")


# -----------------------------
# Main Program
# -----------------------------
def main():
    portfolio = {}

    while True:
        print("\n" + "=" * 45)
        print("          STOCK PORTFOLIO TRACKER")
        print("=" * 45)

        print("1. View Available Stocks")
        print("2. Add Stock")
        print("3. View Portfolio")
        print("4. Save Portfolio Report")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            display_stocks()

        elif choice == "2":
            add_stock(portfolio)

        elif choice == "3":
            display_portfolio(portfolio)

        elif choice == "4":
            save_portfolio(portfolio)

        elif choice == "5":
            print("\nThank you for using Stock Portfolio Tracker!")
            print("Good luck with your CodeAlpha internship!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 5.")


# -----------------------------
# Program Entry Point
# -----------------------------
if __name__ == "__main__":
    main()