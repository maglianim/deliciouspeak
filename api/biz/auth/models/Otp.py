from api.biz.core.models.BaseEntity import BaseEntity
import sqlalchemy
from datetime import date

class Otp(BaseEntity):
    """
    Domain class of Otp entry
    """
    __tablename__ = 'Otp_entries'

    otp = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    user_name = sqlalchemy.Column(sqlalchemy.String)

    def __init__(self, otp=None, user_name=None) -> None:
        self.otp = otp
        self.user_name = user_name
    