import time
from jose import JWTError, jwt
from werkzeug.exceptions import Unauthorized

JWT_ISSUER = "com.api.deliciouspeak"
JWT_SECRET = 'S3cr3t-V4lu3-F0r-T0k3N'
JWT_LIFETIME_SECONDS = 300
JWT_ALGORITHM = "HS256"


def generate_token(user_id):
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(user_id),
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        raise Unauthorized from e


def _current_timestamp() -> int:
    return int(time.time())
   