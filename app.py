from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        "backgroundColor": "#0f172a",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif"
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            id="app-header",
            style={
                "textAlign": "center",
                "color": "#f8fafc",
                "marginBottom": "10px"
            }
        ),

        html.P(
            "Explore Pink Morsel sales by region.",
            style={
                "textAlign": "center",
                "color": "#cbd5e1",
                "marginBottom": "30px",
                "fontSize": "18px"
            }
        ),

        html.Div(
            style={
                "width": "80%",
                "margin": "0 auto 25px auto",
                "backgroundColor": "#1e293b",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.25)"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={
                        "color": "#f8fafc",
                        "fontSize": "18px",
                        "display": "block",
                        "marginBottom": "12px"
                    }
                ),
                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    labelStyle={
                        "marginRight": "20px",
                        "color": "#e2e8f0",
                        "fontSize": "16px"
                    },
                    inputStyle={"marginRight": "6px"}
                ),
            ]
        ),

        html.Div(
            style={
                "width": "90%",
                "margin": "0 auto",
                "backgroundColor": "#1e293b",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.25)"
            },
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

# Callback to update chart
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df.copy()
        title = "Total Daily Pink Morsel Sales - All Regions"
    else:
        filtered_df = df[df["region"] == selected_region].copy()
        title = f"Total Daily Pink Morsel Sales - {selected_region.capitalize()} Region"

    daily_sales = filtered_df.groupby("date", as_index=False)["sales"].sum()
    daily_sales = daily_sales.sort_values("date")

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title=title,
        labels={"date": "Date", "sales": "Total Sales"}
    )

    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#1e293b",
        font_color="#f8fafc",
        title_font_size=22,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)