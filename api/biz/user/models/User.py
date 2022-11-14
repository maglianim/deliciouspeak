from api.biz.core.models.BaseEntity import BaseEntity
import sqlalchemy
from datetime import date

class User(BaseEntity):
    """
    Domain class of user
    """
    __tablename__ = 'User'

    email_address = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String)
    last_name = sqlalchemy.Column(sqlalchemy.String)
    favourite_dish = sqlalchemy.Column(sqlalchemy.String)
    birth_date = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    enable_two_factor = sqlalchemy.Column(sqlalchemy.Boolean)

    def __init__(self, first_name=None, last_name=None, favourite_dish=None, birth_date=None, email_address=None, password=None, enable_two_factor=None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.favourite_dish = favourite_dish
        self.birth_date = birth_date
        self.email_address = email_address
        self.password = password
        self.enable_two_factor = enable_two_factor
    