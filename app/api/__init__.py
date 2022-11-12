'''
Main api entry point
'''
from flask import Blueprint
from api.auth import auth_v1

api_blueprint = Blueprint('api', __name__)

api_blueprint.register_blueprint(auth_v1, url_prefix="/auth/v1")
