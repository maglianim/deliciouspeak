from werkzeug.security import generate_password_hash, check_password_hash

def encode_password(password: str) -> str:
    return generate_password_hash(password, method='sha256')

def check_password(password: str, encoded_password: str) -> bool:
    return check_password_hash(encoded_password, password)
