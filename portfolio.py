import csv
import io

def main():
    portfolio = []

    print("===== STOCK PORTFOLIO TRACKER =====")

    while True:
        ticker = input(
            "\nEnter stock ticker (or 'done' to finish): "
        ).strip().upper()

        if ticker == "DONE":
            if not portfolio:
                print("Please enter at least one stock.")
                continue
            break

        if not ticker:
            print("Ticker cannot be empty.")
            continue

        try:
            buy_price = float(input("Enter buying price per share: "))
            shares = int(input("Enter number of shares: "))
            current_price = float(
                input("Enter current price per share: ")
            )

            if buy_price <= 0 or shares <= 0 or current_price < 0:
                print("Invalid values. Please try again.")
                continue

        except ValueError:
            print("Enter valid numeric values.")
            continue

        invested = buy_price * shares
        current_value = current_price * shares
        profit_loss = current_value - invested
        percentage = (profit_loss / invested) * 100

        portfolio.append({
            "Ticker": ticker,
            "Buy Price": buy_price,
            "Shares": shares,
            "Current Price": current_price,
            "Invested": invested,
            "Current Value": current_value,
            "Profit/Loss": profit_loss,
            "Gain/Loss (%)": percentage
        })

        print(ticker, "added successfully!")

    total_invested = sum(s["Invested"] for s in portfolio)
    total_value = sum(s["Current Value"] for s in portfolio)
    total_profit = total_value - total_invested

    print("\n===== PORTFOLIO SUMMARY =====")

    for stock in portfolio:
        print("\nStock:", stock["Ticker"])
        print("Invested: Rs. {:.2f}".format(stock["Invested"]))
        print("Current Value: Rs. {:.2f}".format(stock["Current Value"]))
        print("Profit/Loss: Rs. {:.2f}".format(stock["Profit/Loss"]))
        print("Gain/Loss: {:.2f}%".format(stock["Gain/Loss (%)"]))

    print("\n===== TOTALS =====")
    print("Total Investment: Rs. {:.2f}".format(total_invested))
    print("Total Market Value: Rs. {:.2f}".format(total_value))
    print("Total Profit/Loss: Rs. {:.2f}".format(total_profit))

    fields = [
        "Ticker", "Buy Price", "Shares", "Current Price",
        "Invested", "Current Value", "Profit/Loss",
        "Gain/Loss (%)"
    ]

    csv_output = io.StringIO()
    writer = csv.DictWriter(csv_output, fieldnames=fields)
    writer.writeheader()
    writer.writerows(portfolio)
    csv_content = csv_output.getvalue()

    try:
        with open("/tmp/portfolio_summary.csv", "w", newline="") as file:
            file.write(csv_content)
        print("\nCSV saved to /tmp/portfolio_summary.csv")
    except OSError:
        print("\nFile saving is restricted by this online compiler.")

    print("\n===== CSV CONTENT =====")
    print(csv_content)

if __name__ == "__main__":
    main()
