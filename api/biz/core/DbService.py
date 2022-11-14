from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship, backref, sessionmaker
from api.biz.core.models.BaseEntity import BaseEntity
from api.biz.user.models.User import User

class DbService(object):
    def __init__(self) -> None:
        engine = create_engine("sqlite:///./api/db/mydb.sqlite")
        BaseEntity.metadata.create_all(engine, checkfirst=True)

    def test_ins_user(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        session.clo

        a1 = User()
        a1.email_address= 'email_address'
        a1.first_name= 'first_name'
        a1.last_name= 'last_name'
        a1.favourite_dish= 'favourite_dish'
        a1.birth_date= 'birth_date'
        a1.password= 'password'
        a1.enable_two_factor = True
        session.add(a1)
        session.commit()