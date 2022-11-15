import math, random
from api.biz.user.models.User import User
from api.biz.auth.models.Otp import Otp
from api.biz.core.BaseService import BaseService
from api.biz.core.MailService import MailService
from api.biz.user.services.UserService import UserService
from api.biz.utils.utility_functions import *
from api.biz.utils import jwt
from sqlalchemy import delete, select
class AuthService(BaseService):
    def __init__(self) -> None:
        super(AuthService, self).__init__()
        self.__user_service = UserService()
        self.__mail_service = MailService()

    def login(self, username: str, password: str):
        """
        performs user login
        """

        if not username or not password:
            return (False, '')
        user = self.__user_service.get_by_email_address(username)
        if not user:
            return (False, '')
        if not check_password(password, user.password):
            return (False, '')

        if not user.enable_two_factor:
            return (True, jwt.generate_token(user.email_address))

        self.__second_factor_auth(user.email_address)
    
        return (True, None)


    def login2fa(self, user_name: str, otp: str) -> str:
        if not user_name or not otp:
            return None
        try:
            session = self._get_session()

            statement = select(Otp).filter_by(otp=otp)
            readed_otp = session.execute(statement).scalars().first()
            if not isinstance(readed_otp, Otp) or readed_otp.user_name != user_name:
                return None
            statement = delete(Otp).filter_by(otp=otp)
            session.execute(statement)
            session.commit()
            return jwt.generate_token(user_name)
        finally:
            session.close()


    def __second_factor_auth(self, user_name):
        """
        invalidates existing otps for the user
        generates a new valid otp
        send the opt to the given mail address
        """
        try:
            session = self._get_session()
            otp = Otp(otp=self.__generate_otp(), user_name=user_name)
            statement = delete(Otp).filter_by(user_name=user_name)
            session.execute(statement)
            session.add(otp)
            session.commit()
            self.__mail_service.send(otp.user_name, 'your OTP', otp.otp)
        finally:
            session.close()

    def __generate_otp(self):
        """
        logic to generate a dummy otp
        """
        digits = "0123456789"
        result = ""

        for i in range(4) :
            result += digits[math.floor(random.random() * 10)]

        return str(result)
