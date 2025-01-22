#app.py


import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Sample excel
sample_data = {
    "Commodity": ["Gold", "Silver", "Oil", "Natural Gas"] * 50,  # Repeated 50 times
    "Date": pd.date_range("2023-01-01", periods=200, freq="W"),  # Weekly data
    "Price": (
        [1850 + i * 5 for i in range(50)] +       # Gold prices
        [24 + i * 0.5 for i in range(50)] +      # Silver prices
        [75 + i for i in range(50)] +            # Oil prices
        [3.5 + i * 0.1 for i in range(50)]       # Natural Gas prices
    ),
}
commodity_df = pd.DataFrame(sample_data)
# load data from the sample excel

commodity_df = pd.DataFrame(sample_data)

# External stylesheets
external_stylesheets = [
    {"href": "https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap", "rel": "stylesheet"},
    dbc.themes.BOOTSTRAP,
]

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.title = "Commodity Dashboard"

# Sidebar layout
sidebar = html.Div(
    [
        html.H2("My App", className="display-4", style={"textAlign": "center", "font-variant": "small-caps"}),
        html.Hr(),
        html.H3("Commodities Analysis", className="display-8", style={"textAlign": "center"}),
        dbc.Nav(
            [
                dbc.NavLink("Page 1", href="/", active="exact"),
                dbc.NavLink("Page 2", href="/page2_url", active="exact"),
            ],
            vertical=True,
            pills=True,
            style={"font-size": 16, "textAlign": "center"},
        ),
    ],
    className="sidebar_style",
        style={
        "width": "140px",         # or "10rem", "20%", etc.
        "padding": "8px",        # optional
        "backgroundColor": "#f8f9fa"  # optional
    }
)

# Content layout
CONTENT_STYLE = {
    "margin-left": "9rem",
    "margin-right": "0.1rem",
    "padding": "0.5rem 0.1rem",
}

# Page 1 content with 4 graphs in a 2x2 layout
page1_content = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="graph1", style={"height": "360px"}), width=6),
                dbc.Col(dcc.Graph(id="graph2", style={"height": "360px"}), width=6),
            ],
            className="mb-3",  # Adjusted margin-bottom for spacing
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="graph3", style={"height": "360px"}), width=6),
                dbc.Col(dcc.Graph(id="graph4", style={"height": "360px"}), width=6),
            ]
        ),
    ],
    style={"padding": "0.1rem"},
)

# Page 2 content (placeholder)
from main9 import page2_table
page2_content = page2_table #html.Div("Page 2 content")




# Main layout
content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Callbacks
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def render_page_content(pathname):
    if pathname == "/":
        return page1_content
    elif pathname == "/page2_url":
        return page2_content
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised."),
        ]
    )

#const config = {
#  displayModeBar: false, // this is the line that hides the bar.
#};

#function toDate(d) {
#	var parts = d.split('/');
#  return new Date(parts[2], parts[0], parts[1]).getTime();
#} 

@app.callback(
    [Output("graph1", "figure"), Output("graph2", "figure"), Output("graph3", "figure"), Output("graph4", "figure")],
    Input("url", "pathname"),
)
def update_graphs(pathname):
    if pathname == "/":

    
        # -----------------------------------------------------------------------------
        # 1. Create the initial line figure
        # -----------------------------------------------------------------------------
        fig1 = px.line(
            commodity_df[commodity_df["Commodity"] == "Gold"],
            x="Date",
            y="Price",
            labels={"Price": "", "Date": ""},
            template="plotly_white",
        )

        # -----------------------------------------------------------------------------
        # 2. Update trace style (color, line width, etc.)
        # -----------------------------------------------------------------------------
        fig1.update_traces(
            line_color="darkgoldenrod",
            line_width=2
        )

        # -----------------------------------------------------------------------------
        # 3. Update layout (axes, margins, background, font)
        # -----------------------------------------------------------------------------
        fig1.update_layout(
            xaxis=dict(
                showgrid=True,
                gridcolor="lightgrey",
                showline=True,
                linewidth=1,
                linecolor="black",
                ticks="outside",
                ticklen=6,
                tickwidth=1.5,
                nticks=20,
            ),
            #margin=dict(l=2, r=2, t=2, b=2),
            yaxis=dict(
                showgrid=True,
                gridcolor="lightgrey",
                showline=True,
                linewidth=1,
                linecolor="black",
                ticks="outside",
                ticklen=6,
                tickwidth=1.5,
            ),
            plot_bgcolor="white",
            margin=dict(t=100, b=1, l=0, r=1),  # extra top margin for the green bar
            font=dict(family="Lato, sans-serif", size=12, color="black"),
        )

        # -----------------------------------------------------------------------------
        # 4. Add a green rectangle at the top (in "paper" coordinates)
        # -----------------------------------------------------------------------------
        fig1.add_shape(
            type="rect",
            xref="paper",
            yref="paper",
            x0=0,
            y0=1.20,   # top boundary (outside the normal plot area)
            x1=1,
            y1=1.05,  # bottom boundary of the rectangle
            fillcolor="darkgreen",
            line=dict(width=0),   # no outline
            layer="below"         # place behind the chart elements
        )

        # -----------------------------------------------------------------------------
        # 5. Add text (annotation) inside the green shape
        # -----------------------------------------------------------------------------
        fig1.add_annotation(
            text="Gold Price",
            x=0.5,          # center the text (paper coordinates range from 0 to 1)
            y=1.18,        # vertically center it between y=1.15 and y=1.3
            xref="paper",
            yref="paper",
            showarrow=False,
            font=dict(size=14, color="white"),
            align="center",
            bgcolor="darkgreen",  # match the shape color so it looks seamless
            borderwidth=0,
        )
        
        fig1.add_annotation(x=pd.to_datetime("31-12-2024"),
                              y=24,
                              text="label1",
                              showarrow=True,
                              arrowhead=1)
        
        fig2 = px.line(
            commodity_df[commodity_df["Commodity"] == "Silver"], x="Date", y="Price", title="Silver Prices"
        )
        fig3 = px.line(
            commodity_df[commodity_df["Commodity"] == "Oil"], x="Date", y="Price", title="Oil Prices"
        )
        fig4 = px.line(
            commodity_df[commodity_df["Commodity"] == "Natural Gas"], x="Date", y="Price", title="Natural Gas Prices"
        )
        return fig1, fig2, fig3, fig4
    # Skip updates if not on the correct page
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update


#if __name__ == "__main__":
#    app.run_server(debug=True)

server = app.server

