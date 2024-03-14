# Import necessary libraries
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback_context

# Load data
data = (
    pd.read_csv("all_stocks_5yr.csv")
    .assign(Date=lambda data: pd.to_datetime(data["date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)
data.set_index('date', inplace=True)
companies = data["Name"].sort_values().unique()

# External stylesheets
external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"]

# Initialize Dash app
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "S&P500 Analytics"

# Define app layout
app.layout =  html.Div( 
    children=[ 
        html.Div(
            children=[
                html.H1("S&P500 Analytics", className="header-title"),
                html.P("Analyse the behavior of S&P500 stock prices between 2013 to 2018", className="header-description"),
                ],
                className="header",
                ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div("Company", className="menu-title"),
                        dcc.Dropdown(
                            id="company-filter",
                            options=[{"label": company, "value": company} for company in companies],
                            value="GOOGL",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div("Date Range", className="menu-title"),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=min(data.index),
                            max_date_allowed=max(data.index),
                            start_date=min(data.index),
                            end_date=max(data.index),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(id="price-chart", config={"displayModeBar": False}),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(id="volume-chart", config={"displayModeBar": False}),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

# Callback to update price chart
@app.callback(
    Output("price-chart", "figure"),
    [Input("company-filter", "value"), Input("date-range", "start_date"), Input("date-range", "end_date")],
)
def update_price_chart(company, start_date, end_date):
    if not company or not start_date or not end_date:
        raise Dash.exceptions.PreventUpdate

    filtered_data = data.loc[start_date:end_date]
    filtered_data = filtered_data[filtered_data["Name"] == company]

    price_chart_figure = {
        "data": [
            {"x": filtered_data.index, "y": filtered_data["close"], "type": "lines", "hovertemplate": "$%{y:.2f}<extra></extra>"},
        ],
        "layout": {
            "title": {"text": "Closing Price of Stocks", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17b897"],
        },
    }
    return price_chart_figure

# Callback to update volume chart
@app.callback(
    Output("volume-chart", "figure"),
    [Input("company-filter", "value"), Input("date-range", "start_date"), Input("date-range", "end_date")],
)
def update_volume_chart(company, start_date, end_date):
    if not company or not start_date or not end_date:
        raise Dash.exceptions.PreventUpdate

    filtered_data = data.loc[start_date:end_date]
    filtered_data = filtered_data[filtered_data["Name"] == company]

    volume_chart_figure = {
        "data": [
            {"x": filtered_data.index, "y": filtered_data["volume"], "type": "bar", "marker": {"color": "#636efa"}},
        ],
        "layout": {
            "title": {"text": "Volume Traded", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#636efa"],
        },
    }
    return volume_chart_figure

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
