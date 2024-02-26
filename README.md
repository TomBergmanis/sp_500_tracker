# sp_500_tracker

A python project that tracks S and P 500 companies and allows for comparison
Stock Data Analysis and Comparison

This script allows users to fetch and compare stock data for companies in the S&P 500 index.

Dependencies:

- yfinance: A Python library to interact with Yahoo Finance for fetching stock data.
- matplotlib: A plotting library for creating visualizations.

Functions:

1. get_stock_data(ticker, start_date, end_date):

   - Fetches historical stock data for a given stock ticker symbol within a specified date range.
   - Parameters:
     - ticker (str): Stock ticker symbol.
     - start_date (str): Start date for data retrieval in the format 'YYYY-MM-DD'.
     - end_date (str): End date for data retrieval in the format 'YYYY-MM-DD'.
   - Returns:
     - stock_data (pandas.DataFrame): DataFrame containing historical stock data (Open, High, Low, Close, Volume).

2. plot_multiple_stocks(stock_data_list, title):
   - Plots the closing prices of multiple stocks on a single graph.
   - Parameters:
     - stock_data_list (list): List of tuples containing (stock_data, ticker) pairs.
     - title (str): Title for the plot.
   - Displays the plot with the closing prices of each stock over time.

Main Execution:

- The script continuously prompts the user to enter a stock ticker symbol in the S&P 500.
- It fetches and stores the historical stock data for each entered stock.
- The user can visualize the closing prices of the added stocks on a single graph.
- The script allows the user to add more companies for comparison or exit the loop.

Usage:

- Run the script.
- Enter a stock ticker symbol when prompted. Press Enter to finish.
- Visualize the closing prices on the plot.
- Optionally, add more companies for comparison.
- Exit the loop when done.

Note: Ensure the required dependencies (yfinance and matplotlib) are installed before running the script.
