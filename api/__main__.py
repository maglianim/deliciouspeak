import connexion

from api import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('deliciouspeak.yaml',
                arguments={'title': 'deliciouSpeak API'},
                base_path='/api',
                pythonic_params=True)

    app.run(port=5000)
    print(app)


if __name__ == '__main__':
    main()
