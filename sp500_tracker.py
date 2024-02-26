import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_data(ticker, start_date, end_date):
    try:
        # Get stock data from Yahoo Finance using the yfinance library
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        # Handle any exceptions that may occur during data retrieval
        print(f"Error fetching stock data for {ticker}: {e}")
        return None

def plot_multiple_stocks(stock_data_list, title):
    # Plotting multiple stock data on a single graph
    plt.figure(figsize=(10, 6))

    # Iterate through each stock data in the list and plot its closing prices
    for stock_data, ticker in stock_data_list:
        plt.plot(stock_data['Close'], label=ticker)

    # Set plot title, x-axis label, y-axis label, legend, and grid
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    stock_data_list = []  # List to store stock data and tickers

    while True:
        # Input parameters for date range
        start_date = "2020-01-01"
        end_date = "2024-01-01"

        # Get user input for the stock ticker symbol
        stock_ticker = input("Enter a stock ticker symbol in the S&P 500 (press Enter to finish): ").strip()

        if not stock_ticker:
            break  # Exit the loop if the user presses Enter without entering a stock ticker

        # Check if the company is already in the list
        if any(ticker.lower() == stock_ticker.lower() for _, ticker in stock_data_list):
            print("Company already added. Please choose a different company.")
            continue

        # Fetch data for the entered stock ticker
        stock_data = get_stock_data(stock_ticker, start_date, end_date)

        if stock_data is not None:
            # Add the stock data and ticker to the list
            stock_data_list.append((stock_data, stock_ticker))

            # Plot data for all added stocks
            plot_multiple_stocks(stock_data_list, 'Stock Comparison')

            # Ask if the user wants to add, remove, or finish
            action = input("Do you want to add another company (add), remove a company (remove), or finish (finish): ").strip().lower()

            if action == 'finish':
                break  # Exit the loop if the user chooses to finish
            elif action == 'remove':
                # Display the current list of companies for removal
                print("Companies currently on the graph:")
                for i, (_, ticker) in enumerate(stock_data_list):
                    print(f"{i + 1}. {ticker}")

                try:
                    # Get the index of the company to remove
                    remove_index = int(input("Enter the number of the company you want to remove: ")) - 1

                    # Remove the selected company
                    if 0 <= remove_index < len(stock_data_list):
                        del stock_data_list[remove_index]
                        print("Company removed.")
                    else:
                        print("Invalid selection. No company removed.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    # Final plot after user finishes or decides not to add more
    if stock_data_list:
        plot_multiple_stocks(stock_data_list, 'Final Stock Comparison')
