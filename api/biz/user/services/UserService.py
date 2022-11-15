"""
Business logic for the user entity
"""

from api.biz.user.models.User import User
from api.biz.core.BaseService import BaseService
from sqlalchemy import select
from  api.biz.core.models.exceptions import *
from api.biz.utils.utility_functions import *
PWD_MIN_ACCEPTED_LENGTH = 8

class UserService(BaseService):
    def __init__(self) -> None:
        super(UserService, self).__init__()

    def create(self, user: User) -> bool:
        """
        creates a new user
        """

        self.__validateUser(user)
        try:
            session = self._get_session()
            existing_user = self.get_by_email_address(user.email_address)
            if existing_user:
                raise ResourceExistingException('User already exists')
            user.password = encode_password(user.password)
            session.add(user)
            session.commit()
            return True
        finally:
            session.close()
        

    def get_by_email_address(self, email_address: str) -> User:
        """
        select the user from the db by its email address
        """
        try:
            session = self._get_session()
            statement = select(User).filter_by(email_address=email_address)
            result = session.execute(statement).scalars().first()
            if isinstance(result, User):
                return result
            return None
        finally:
            session.close()

    def __validateUser(self, user: User):
        """
        Validates the user. as example purpose it only checks if
        - email_address is provided
        - password is provided and has a minimum length.
        """
        if not user.email_address:
            raise InvalidUserException('Invalid password')
        if not user.password or len(user.password) < PWD_MIN_ACCEPTED_LENGTH:
            raise InvalidUserException('Invalid password')