from api.biz.user.models.User import User
from api.biz.core.BaseService import BaseService
from api.biz.user.services.UserService import UserService
from api.biz.utils.utility_functions import *

class AuthService(BaseService):
    def __init__(self) -> None:
        super(AuthService, self).__init__()
        self.__user_service = UserService()

    def login(self, username: str, password: str):
        """
        performs user login
        """

        if not username or not password:
            return (False, '')
        user = self.__user_service.get_by_email_address(username)
        if not user:
            return (False, '')
        print(user.enable_two_factor)
        if not check_password(password, user.password):
            return (False, '')

        if not user.enable_two_factor:
            return (True, 'jsdkjf8734fuyh87hgf')
        
        return (True, None)            
