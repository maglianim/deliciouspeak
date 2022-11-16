import sys
from werkzeug.security import generate_password_hash, check_password_hash

def encode_password(password: str) -> str:
    return generate_password_hash(password, method='sha256')

def check_password(password: str, encoded_password: str) -> bool:
    return check_password_hash(encoded_password, password)

 
def print_to_stdout(*a):
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file=sys.stdout)