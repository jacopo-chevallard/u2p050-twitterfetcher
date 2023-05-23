from flask import make_response, request
import json

from . import api_bp

@api_bp.route("/print_hello", methods=["GET"])
def print_hello():
    person_name = request.args.get('person_name', 'World')
    return make_response(json.dumps({"hello": person_name}), 200)