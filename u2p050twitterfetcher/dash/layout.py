import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
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
        html.H2("Please enter your Twitter query:", style={'text-align': 'center'}),  # Instructions
        html.Hr(),
        html.Div([
            html.Div([
                    html.Label("Choose the data collection approach:", style={'margin-right': '10px'}),  # Add explanation
                    dcc.RadioItems(  # Add RadioItems here
                        id='toggle',
                        options=[{'label': 'Fetch', 'value': 'fetch'}, {'label': 'Stream', 'value': 'stream'}],
                        value='fetch',  # Default value
                        inline=True  # Display options inline
                    )
                ],
                style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'margin-bottom': '20px'}  # Center items
            ),
            html.Div([
                dmc.Textarea(id='msg_input', autosize=True, minRows=4, maxRows=8, 
                            style={'flex': '12', 'height': '100px', 'margin-right': '10px', 'font-size': '1.8rem'}),
                html.Button('Send', id='send_button', type='submit',
                            style={'flex': '1', 'height': '40px'})
                ],
                style={'display': 'flex', 'width': '90%', 'margin': '0 auto', 'margin-bottom': '10px'}),
            html.Br(),
            html.Div(id='conversation', style={'width': '90%', 'margin': '0 auto', 'overflow': 'auto'}),
        ],
        id='screen',
        style={'width': '100%', 'margin': '0 auto'})
    ], style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'})



    return layout
