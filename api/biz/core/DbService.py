from sqlalchemy import *
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from api.biz.core.models.BaseEntity import BaseEntity

class DbService(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DbService, cls).__new__(cls)
            cls.instance.engine = create_engine("sqlite:///./api/db/mydb.sqlite")
            BaseEntity.metadata.create_all(cls.instance.engine, checkfirst=True)
            session_factory = sessionmaker(bind=cls.instance.engine)
            cls.instance.Session = scoped_session(session_factory)
        return cls.instance

    def get_session(self) -> Session:
        """
        returns a new db session
        """
        return self.Session()
