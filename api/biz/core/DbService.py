from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import relationship, Session
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session
from api.biz.core.models.BaseEntity import BaseEntity
from api.biz.user.models.User import User

class DbService(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DbService, cls).__new__(cls)
            cls.instance.abc = 'sdfsdf'
            cls.instance.engine = create_engine("sqlite:///./api/db/mydb.sqlite")
            BaseEntity.metadata.create_all(cls.instance.engine, checkfirst=True)
            session_factory = sessionmaker(bind=cls.instance.engine)
            cls.instance.Session = scoped_session(session_factory)
        return cls.instance

    def get_session(self) -> Session:
        return self.Session()

# def test_ins_user():
#     session = DbService().Session()

#     a1 = User()
#     a1.email_address= 'email_address'
#     a1.first_name= 'first_name'
#     a1.last_name= 'last_name'
#     a1.favourite_dish= 'favourite_dish'
#     a1.birth_date= 'birth_date'
#     a1.password= 'password'
#     a1.enable_two_factor = True
#     session.add(a1)
#     a2 = User()
#     a2.email_address= 'email_address_2'
#     a2.first_name= 'first_name'
#     a2.last_name= 'last_name'
#     a2.favourite_dish= 'favourite_dish'
#     a2.birth_date= 'birth_date'
#     a2.password= 'password'
#     a2.enable_two_factor = True
#     session.add(a2)
#     session.commit()