from api.biz.user.models.User import User

class AuthService(object):
    def __init__(self) -> None:
        pass

    def add(self, user: User):
        """
        adds a user
        """
        
        print('usser!!!!!!!!!!!!!!!')
        print(user)