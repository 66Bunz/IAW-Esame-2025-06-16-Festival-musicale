from flask import Blueprint

tickets_bp = Blueprint('tickets', __name__, url_prefix='/tickets')

from blueprints.tickets import routes