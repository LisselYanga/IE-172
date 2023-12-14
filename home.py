import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from app import app

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

layout = html.Div(
    [
        html.H2('Welcome to NAM Dental Clinic!', style={'color': CUSTOM_COLORS['primary']}),
        html.Hr(style={'background-color': CUSTOM_COLORS['primary']}),
        html.Div(
            [
                html.Span(
                    "This is the official website of NAM Dental Clinic",
                ),
                html.Br(),
            ],
            style={'width': '50%', 'float': 'left', 'color': CUSTOM_COLORS['dark']}
        ),
        html.Div(
            [
                html.Label('Username', style={'color': CUSTOM_COLORS['dark']}),
                dbc.Input(id='login-textbox', type='text', placeholder='Enter your username', style={'background-color': CUSTOM_COLORS['light']}),
                html.Br(),
                html.Label('Password', style={'color': CUSTOM_COLORS['dark']}),
                dbc.Input(
                    id='password-textbox',
                    type='password',
                    placeholder='Enter your password',
                    className='mt-3',
                    style={'background-color': CUSTOM_COLORS['light']},
                ),
                html.Br(),
                dbc.Button('Login', id='login-button', color='primary', className='mt-3'),
                html.Div(id='login-output', style={'margin-top': '1em'}),
            ],
            style={'width': '50%', 'float': 'right', 'text-align': 'right', 'padding-left': '10px', 'height': '100%', 'color': CUSTOM_COLORS['dark']}
        ),
        html.Div(
            [
                html.A(
                    dbc.Button('Book your appointment now!', id='book-appointment-button', n_clicks=0, className='btn btn-primary mt-3'),
                    href='https://www.facebook.com/namdentalclinic',
                    target='_blank',  # Open the link in a new tab
                    style={'color': 'white'}  # Text color
                ),
                html.H3('Dental Services', style={'color': CUSTOM_COLORS['primary']}),
                html.Ul(
                    [
                        html.Li("Oral Prophylaxis"),
                        html.Li("Tooth Restoration"),
                        html.Li("Tooth Extraction"),
                        html.Li("Odontectomy"),
                        html.Li("Teeth Whitening/Bleaching"),
                        html.Li("Flouride Treatment"),
                        html.Li("Root Canal Treatment"),
                        html.Li("Prosthesis"),
                        html.Li("Complete Denture"),
                        html.Li("Removable Partial Denture"),
                        html.Li("Crowns & Bridges (Plastic, Porcelain, Ceramage, Emax, Zirconia)"),
                        html.Li("Cosmetic Dentistry (Porcelain Veneers, Laminates)"),
                        html.Li("Orthodontic Treatment (Self-ligating braces)"),
                        html.Li("Retainers"),
                    ],
                    style={'color': CUSTOM_COLORS['dark']}
                ),
            ],
            style={'width': '100%', 'float': 'left', 'padding': '20px'}
        ),
    ],
    style={'width': '100%', 'height': '100%', 'overflow': 'hidden', 'background-color': CUSTOM_COLORS['light']}  # Ensure the entire width and height is used
)


@app.callback(
    Output('login-output', 'children'),
    [Input('login-button', 'n_clicks')],
    [State('login-textbox', 'value'),
     State('password-textbox', 'value')]
)
def check_login(n_clicks, username, password):
    if n_clicks is None:
        raise PreventUpdate

    # Example: Check if the username are provided
    if username and password:
        return dbc.Alert(f"Welcome, {username}! Login successful.")
    else:
        return dbc.Alert("Please enter both username and password.", color='danger')
    
@app.callback(
    Output('book-appointment-button', 'children'),
    [Input('book-appointment-button', 'n_clicks')]
)
def book_appointment(n_clicks):
    if n_clicks is None or n_clicks == 0:
        raise PreventUpdate

    # Example: Add your booking logic here
    return "Booking in progress..."