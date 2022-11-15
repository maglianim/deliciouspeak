from api.biz.user.models.User import User
from api.biz.core.DbService import DbService
from sqlalchemy import select

PWD_MIN_ACCEPTED_LENGTH = 8

class UserService(object):
    def __init__(self) -> None:
        self.__db_service = DbService()
        

    def create(self, user: User) -> int:
        """
        creates a new user
        """

        self.__validateUser(user)
        try:
            session = self.__db_service.get_session()
            existingUser = self.get_by_email_address(user.email_address)
            if (existingUser):
                raise Exception('User already exists')
            session.add(user)
            session.commit()
        finally:
            session.close()
        return 0

    def get_by_email_address(self, email_address: str) -> User:
        try:
            session = self.__db_service.get_session()
            statement = select(User).filter_by(email_address=email_address)
            result = session.execute(statement).scalars().first()
            if isinstance(result, User):
                return result
            return None
        finally:
            session.close()        

    def __validateUser(self, user: User):
        """
        Validates the user. as example purpose it only checks if password is provided and has a minimum length.
        """
        if not user.password or len(user.password) < PWD_MIN_ACCEPTED_LENGTH:
            raise Exception('Invalid password')