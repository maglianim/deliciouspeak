"""
    Main entry point of the api
"""
import connexion

from api import encoder
from biz.core.DbService import DbService

def main():
    """
        Main entry point of the api
    """
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('deliciouspeak.yaml',
                arguments={'title': 'deliciouSpeak API'},
                base_path='/api',
                pythonic_params=True)

    DbService().init()

    app.run(port=5000)

if __name__ == '__main__':
    main()
