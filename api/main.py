"""
    Main entry point of the api
"""
import connexion

from api import encoder
from api.biz.utils import jwt

def decode_token(token):
    """
    main entry point for the decode token utility function
    """
    return jwt.decode_token(token)

def create_app():
    """
    App factory
    """
    app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('deliciouspeak.yaml',
                arguments={'title': 'deliciouSpeak API'},
                base_path='/api',
                pythonic_params=True)
    return app


def main():
    """
        Main entry point of the api
    """
    app = create_app()
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    main()
