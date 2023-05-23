from dash.dependencies import Input, Output
from ..auth.auth import payload_from_token
from ..dash.cache.helpers import store_data_frame, load_data_frame


def register_callbacks(app, cache=None):
    @app.callback()
    def first_callback():
        """
        """

        # Way to secure function
        payload = payload_from_token()

        return()