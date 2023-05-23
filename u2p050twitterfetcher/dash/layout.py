import dash_bootstrap_components as dbc

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

    layout = dbc.Container()

    return layout
