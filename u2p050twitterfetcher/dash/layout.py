import dash_bootstrap_components as dbc
from dash import html, dcc

def apply_layout_with_auth(app):
    """Because Layout must be a dash component or a function that returns a dash component.
    :param dash_app:
    :return:
    """
    app.layout = layout()


def layout():
    """Function to design the layout, can pass arguments like dash_app or server
    :return:
        layout object
    """

    layout = html.Div([
        html.Div([
            html.Div([
                html.P("Please enter your Twitter query:", style={'text-align': 'center'}),  # Instructions
                html.Br(),
                dcc.Input(id='msg_input', value='hello', type='text', debounce=True, n_submit=0, 
                        style={'flex': '12', 'height': '40px', 'margin-right': '10px'}),
                html.Button('Send', id='send_button', type='submit',
                            style={'flex': '1', 'height': '40px'})
                ],
                style={'display': 'flex', 'width': '90%', 'margin': '0 auto', 'margin-bottom': '10px'}),
            html.Br(),
            html.Div(id='conversation', style={'width': '90%', 'margin': '0 auto', 'overflow': 'auto'}),
            ],
            id='screen',
            style={'width': '100%', 'margin': '0 auto'})
    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'})

    return layout
