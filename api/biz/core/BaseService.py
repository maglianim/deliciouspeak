from api.biz.core.DbService import DbService

class BaseService:
    def __init__(self) -> None:
        self.__db_service = DbService()
    
    def _get_session(self):
        return self.__db_service.get_session()
    