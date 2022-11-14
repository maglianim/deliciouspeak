from api.biz.user.models.User import User

PWD_MIN_ACCEPTED_LENGTH = 8

class UserService(object):
    def __init__(self) -> None:
        pass

    def create(self, user: User) -> int:
        """
        creates a new user
        """
       
        print('usser!!!!!!!!!!!!!!!')
        print(user)

        self.__validateUser(user)
        return 0

    def __validateUser(self, user: User):
        """
        Validates the user. as example purpose it only checks if password is provided and has a minimum length.
        """
        if not user.password or len(user.password) < PWD_MIN_ACCEPTED_LENGTH:
            raise Exception('Invalid password')