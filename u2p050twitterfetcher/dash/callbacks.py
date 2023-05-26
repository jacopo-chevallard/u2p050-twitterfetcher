from dash.dependencies import Input, Output, State
from ..auth.auth import payload_from_token
from ..dash.cache.helpers import store_data_frame, load_data_frame
from dash import html, dcc
import urllib.parse
from flask import current_app
import os

def register_callbacks(app, cache=None):

    @app.callback(
        Output(component_id='conversation', component_property='children'),
        Input(component_id='send_button', component_property='n_clicks'),
        Input(component_id="msg_input",component_property="n_submit"),
        State(component_id='msg_input', component_property='value'),
        prevent_initial_call=True
    )
    # function to add new user*bot interaction to conversation history
    def update_conversation(click, n_submit, text):
        # user message aligned left
        rcvd = [dcc.Markdown(f'*{text}*', style={'text-align': 'left'})]

        r = urllib.parse.quote_plus(text)

        # bot response aligned right and italics
        rspd = [dcc.Markdown(f'**{r}**', style={'text-align': 'left'})]

        base_url = current_app.config.get("HEROKU_URL") if current_app.config.get("HEROKU_URL") else "http://127.0.0.1:5000"
        base_url = os.path.join(base_url, "api", "fetch", "twitter")
        full_url = base_url + "?content=" + r

        # Create a clickable link
        clickable_link = html.A(f'{full_url}', href=f'{full_url}', target='_blank')

        output = rcvd + rspd + [html.Hr(), clickable_link]

        return output



    @app.callback(
        Output(component_id='msg_input', component_property='value'),
        [Input(component_id='conversation', component_property='children')]
    )
    def clear_input(_):
        return ''