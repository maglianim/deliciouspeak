# DeliciouSpeak auth service


This is the auth service of the well-known cooking forum deliciouSpeak.

This is a demonstrative app that enables a user to register and perform a login with one-factor or two-factor mode. In case of two-factor authentication a freshly created otp is logged to the stdout.

The api has been developed with a document-first approach. you can find [here](./api/openapi/deliciouspeak.yaml) the api specifications reference.

Internally it uses sqlite to store user credentials; The db is automatically created and configured.


## Setup

### VSCode .devcontainer environment

If you are using Visual studio code you can find an already configured devcontainer which provides to setup all necessary dependency. the only prerequisite is the remote dev container extension. see [Microsoft devcontainer docs](https://code.visualstudio.com/docs/devcontainers/containers).

In this case just select the Action "Open folder in container" inside VS code

### Generic environment

Just install project dependencies and test dependencies:

```sh
pip install -r requirements.txt -r test-requirements.txt
```

## Usage

__Note: This is a demonstrative project so the app is hosted in a demo server and it is started with all debug flags.__

To launch the live debug server just type the following command from the root of the workspace:

```sh
python ./api/main.py
```

To run the the tests type the following command from the root of the workspace:

```sh
python -m unittest discover ./api/test/
```

## Docker image

Along with the codebase there is also a docker file configuration to build project image

To build the image just type the following command from the root of the project:

```sh
docker image build -t deliciouspeak .
```

Now it is possibile to launch the containerized version of the app:

```sh
docker container run -p 5000:5000 -it --rm deliciouspeak
```

It is also possible to bind a local folder to keep database persistent:

```sh
docker container run -v <YOUR_LOCAL_FOLDER>:/app/api/db -p 5000:5000 -it --rm deliciouspeak
```
