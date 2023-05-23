"""Module containing the defintion of the app APIs."""

from flask import Blueprint

api_bp = Blueprint("api", __name__)

# Import views.py to register the routes with api_bp
from . import views