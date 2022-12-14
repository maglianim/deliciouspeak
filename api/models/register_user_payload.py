# coding: utf-8
"""
Auto generated from openapi-generator-cli tool
"""

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api.models.base_model_ import Model
from api import util


class RegisterUserPayload(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, first_name=None, last_name=None, favourite_dish=None, birth_date=None, email_address=None, password=None, enable_two_factor=None):  # noqa: E501
        """RegisterUserPayload - a model defined in OpenAPI

        :param first_name: The first_name of this RegisterUserPayload.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this RegisterUserPayload.  # noqa: E501
        :type last_name: str
        :param favourite_dish: The favourite_dish of this RegisterUserPayload.  # noqa: E501
        :type favourite_dish: str
        :param birth_date: The birth_date of this RegisterUserPayload.  # noqa: E501
        :type birth_date: date
        :param email_address: The email_address of this RegisterUserPayload.  # noqa: E501
        :type email_address: str
        :param password: The password of this RegisterUserPayload.  # noqa: E501
        :type password: str
        :param enable_two_factor: The enable_two_factor of this RegisterUserPayload.  # noqa: E501
        :type enable_two_factor: bool
        """
        self.openapi_types = {
            'first_name': str,
            'last_name': str,
            'favourite_dish': str,
            'birth_date': date,
            'email_address': str,
            'password': str,
            'enable_two_factor': bool
        }

        self.attribute_map = {
            'first_name': 'firstName',
            'last_name': 'lastName',
            'favourite_dish': 'favouriteDish',
            'birth_date': 'birthDate',
            'email_address': 'emailAddress',
            'password': 'password',
            'enable_two_factor': 'enableTwoFactor'
        }

        self._first_name = first_name
        self._last_name = last_name
        self._favourite_dish = favourite_dish
        self._birth_date = birth_date
        self._email_address = email_address
        self._password = password
        self._enable_two_factor = enable_two_factor

    @classmethod
    def from_dict(cls, dikt) -> 'RegisterUserPayload':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RegisterUserPayload of this RegisterUserPayload.  # noqa: E501
        :rtype: RegisterUserPayload
        """
        return util.deserialize_model(dikt, cls)

    @property
    def first_name(self):
        """Gets the first_name of this RegisterUserPayload.

        The first name of the user  # noqa: E501

        :return: The first_name of this RegisterUserPayload.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this RegisterUserPayload.

        The first name of the user  # noqa: E501

        :param first_name: The first_name of this RegisterUserPayload.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this RegisterUserPayload.

        The last name of the user  # noqa: E501

        :return: The last_name of this RegisterUserPayload.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this RegisterUserPayload.

        The last name of the user  # noqa: E501

        :param last_name: The last_name of this RegisterUserPayload.
        :type last_name: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def favourite_dish(self):
        """Gets the favourite_dish of this RegisterUserPayload.

        The favourite dish of the user.  # noqa: E501

        :return: The favourite_dish of this RegisterUserPayload.
        :rtype: str
        """
        return self._favourite_dish

    @favourite_dish.setter
    def favourite_dish(self, favourite_dish):
        """Sets the favourite_dish of this RegisterUserPayload.

        The favourite dish of the user.  # noqa: E501

        :param favourite_dish: The favourite_dish of this RegisterUserPayload.
        :type favourite_dish: str
        """
        if favourite_dish is None:
            raise ValueError("Invalid value for `favourite_dish`, must not be `None`")  # noqa: E501

        self._favourite_dish = favourite_dish

    @property
    def birth_date(self):
        """Gets the birth_date of this RegisterUserPayload.

        The date of birth of the user.  # noqa: E501

        :return: The birth_date of this RegisterUserPayload.
        :rtype: date
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this RegisterUserPayload.

        The date of birth of the user.  # noqa: E501

        :param birth_date: The birth_date of this RegisterUserPayload.
        :type birth_date: date
        """
        if birth_date is None:
            raise ValueError("Invalid value for `birth_date`, must not be `None`")  # noqa: E501

        self._birth_date = birth_date

    @property
    def email_address(self):
        """Gets the email_address of this RegisterUserPayload.

        The email of the user. Note, this will be also the username  # noqa: E501

        :return: The email_address of this RegisterUserPayload.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this RegisterUserPayload.

        The email of the user. Note, this will be also the username  # noqa: E501

        :param email_address: The email_address of this RegisterUserPayload.
        :type email_address: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def password(self):
        """Gets the password of this RegisterUserPayload.

        The password chosen by the user  # noqa: E501

        :return: The password of this RegisterUserPayload.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RegisterUserPayload.

        The password chosen by the user  # noqa: E501

        :param password: The password of this RegisterUserPayload.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def enable_two_factor(self):
        """Gets the enable_two_factor of this RegisterUserPayload.

        Tells the system if two-factor authentication is enabled for the users  # noqa: E501

        :return: The enable_two_factor of this RegisterUserPayload.
        :rtype: bool
        """
        return self._enable_two_factor

    @enable_two_factor.setter
    def enable_two_factor(self, enable_two_factor):
        """Sets the enable_two_factor of this RegisterUserPayload.

        Tells the system if two-factor authentication is enabled for the users  # noqa: E501

        :param enable_two_factor: The enable_two_factor of this RegisterUserPayload.
        :type enable_two_factor: bool
        """
        if enable_two_factor is None:
            raise ValueError("Invalid value for `enable_two_factor`, must not be `None`")  # noqa: E501

        self._enable_two_factor = enable_two_factor
