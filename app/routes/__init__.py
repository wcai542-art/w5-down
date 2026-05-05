from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
task_bp = Blueprint('task', __name__)

from . import auth_routes
from . import task_routes
