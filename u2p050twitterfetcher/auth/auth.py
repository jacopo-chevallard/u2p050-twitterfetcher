import jwt
from functools import wraps
from flask import current_app, request, session, abort

def payload_from_token(token=None):
    """Store the token in session with a priority for the token coming from the hub request.
    Store the dates from the request in session"""
    # These conditions allow the priority for token and other args coming from hub requests
    if token:
        session["token"] = token

    if request.args.get("token"):
        session["token"] = request.args.get("token")

    try:
        token = session.get("token")
        payload = jwt.decode(
            token, key=current_app.config.get("TOKEN_SECRET"), algorithms=["HS256"]
        )
        return payload

    except jwt.ExpiredSignatureError as e:
        print("{}".format(e), flush=True)
        return abort(401)

    except jwt.InvalidTokenError as e:
        print("{}".format(e), flush=True)
        return abort(401)


def valid_auth_required(func):
    """Write comments from login_required"""

    @wraps(func)
    def protect_view_func(*args, **kwargs):
        # token = request.args.get('token') or session.get('token')
        # if payload_from_token(token):
        if payload_from_token():
            return func(*args, **kwargs)

    return protect_view_func