from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv("formatted_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])

daily_sales = df.groupby("date", as_index=False)["sales"].sum()

daily_sales = daily_sales.sort_values("date")

fig = px.line(daily_sales, x="date", y="sales", title="Daily Pink Morsel Sales", labels={"date": "Date", "sales": "Total Sales"})

app = Dash(__name__)

app.layout = html.Div([html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}), dcc.Graph(id="sales-line-chart", figure=fig)])

if __name__ == "__main__":
    app.run(debug=True)