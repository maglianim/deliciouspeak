'''
Main auth api entry point
'''
from flask import Blueprint

auth_v1 = Blueprint('auth_v1', 'auth_v1')

@auth_v1.route("/hello")
def hellov1():
    return 'hello auth v1'
