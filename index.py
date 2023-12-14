from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import webbrowser
from app import app
from apps import home

# Custom color palette
CUSTOM_COLORS = {
    "primary": "#8E44AD",   # Purple
    "secondary": "#9B59B6",  # Darker purple
    "success": "#3498DB",    # Blue
    "info": "#5D6D7E",       # Grayish blue
    "warning": "#F39C12",    # Orange
    "danger": "#E74C3C",     # Red
    "light": "#ECF0F1",      # Light gray
    "dark": "#2C3E50"        # Dark gray
}

# Apply the custom color palette to specific components
navbar_style = {"background-color": CUSTOM_COLORS["primary"]}
content_style = {"background-color": CUSTOM_COLORS["light"]}

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=True),
        html.Div(id='page-content', style=content_style),
    ],
    style=content_style
)


@app.callback(
    [Output('page-content', 'children')
    ],
    [
        Input('url', 'pathname')
    ]
)
def displaypage (pathname):
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]
        if eventid == 'url':
            if pathname == '/' or pathname == '/home':
                returnlayout = home.layout
            elif pathname == '/movies':
                returnlayout = 'moviepage'
            else:
                returnlayout = 'error404'

            return [returnlayout]
        else:
            raise PreventUpdate
    else:
        raise PreventUpdate



if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)