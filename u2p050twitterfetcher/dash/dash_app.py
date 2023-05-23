import dash_bootstrap_components as dbc
from dash_extensions.enrich import DashProxy

from .callbacks import register_callbacks
from .layout import apply_layout_with_auth

def init_dash(server, cache=None):
    """Create a Plotly Dash dash_app."""
    dash_app = DashProxy(
        server=server,
        routes_pathname_prefix="/u2p050twitterfetcher/dashboard/",
        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

    apply_layout_with_auth(dash_app)
    register_callbacks(dash_app, cache=cache)

    return dash_app.server