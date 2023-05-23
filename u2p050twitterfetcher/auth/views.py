from . import auth_bp 
from .auth import payload_from_token, valid_auth_required
from flask import make_response, abort


@auth_bp.route("/healthz")
def sanity_check():
    return "app is healthy", 200


@auth_bp.route("/token_check")
@valid_auth_required
def check_token():
    try:
        payload = payload_from_token()
        response = make_response(str(payload))

        return response, 200
    except:
        return abort(401)
