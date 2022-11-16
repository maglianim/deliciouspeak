from api.models.register_user_payload import RegisterUserPayload
from api.biz.user.models.User import User

def from_register_userpayload_to_user(from_obj: RegisterUserPayload) -> User:
    result = User(email_address=from_obj.email_address,
                    first_name=from_obj.first_name,
                    last_name=from_obj.last_name,
                    favourite_dish=from_obj.favourite_dish,
                    birth_date=from_obj.birth_date,
                    password=from_obj.password,
                    enable_two_factor=from_obj.enable_two_factor)
    return result
