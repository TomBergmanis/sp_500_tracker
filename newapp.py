import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import yfinance as yf
import os

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
    fig = dcc.Graph(
        figure={
            'data': [
                {'x': stock_data.index, 'y': stock_data['Close'], 'type': 'line', 'name': ticker}
                for stock_data, ticker in stock_data_list
            ],
            'layout': {
                'title': title,
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Closing Price'},
                'legend': {'traceorder': 'normal'}
            }
        }
    )
    return fig

def main():
    newapp = dash.Dash(__name__)

    stock_data_list = []  # List to store stock data and tickers

    @newapp.callback(
        Output('stock-graph', 'figure'),
        [Input('add-button', 'n_clicks')],
        [dash.dependencies.State('stock-ticker', 'value')]
    )
    def add_stock(n_clicks, stock_ticker):
        if stock_ticker:
            # Check if the company is already in the list
            if any(ticker.lower() == stock_ticker.lower() for _, ticker in stock_data_list):
                print("Company already added. Please choose a different company.")
            else:
                # Fetch data for the entered stock ticker
                stock_data = get_stock_data(stock_ticker, start_date, end_date)

                if stock_data is not None:
                    # Add the stock data and ticker to the list
                    stock_data_list.append((stock_data, stock_ticker))

        return plot_multiple_stocks(stock_data_list, 'Stock Comparison')

    newapp.layout = html.Div([
        html.H1("Stock Comparison"),
        html.Div([
            dcc.Input(id='stock-ticker', type='text', placeholder='Enter stock ticker'),
            html.Button(id='add-button', n_clicks=0, children='Add Stock')
        ]),
        dcc.Graph(id='stock-graph')
    ])

    if __name__ == '__main__':
        newapp.run_server(debug=True)


if __name__ == "__main__":
    main()
