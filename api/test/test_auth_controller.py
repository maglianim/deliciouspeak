# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from api.models.auth_login200_response import AuthLogin200Response  # noqa: E501
from api.models.login2fa_payload import Login2faPayload  # noqa: E501
from api.models.login_payload import LoginPayload  # noqa: E501
from api.models.login_success_resp import LoginSuccessResp  # noqa: E501
from api.models.register_user_payload import RegisterUserPayload  # noqa: E501
from api.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_auth_login(self):
        """Test case for auth_login

        Logs a user inside the system
        """
        login_payload = {"password":"very-strong-password","username":"john.smith@delicious.com"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MAGLIANIM_1/oauth-pwd/1.0.0/auth/login',
            method='POST',
            headers=headers,
            data=json.dumps(login_payload),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_login2fa_post(self):
        """Test case for auth_login2fa_post

        performs two factor login
        """
        login2fa_payload = {"otp":"abcdefg"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MAGLIANIM_1/oauth-pwd/1.0.0/auth/login2fa',
            method='POST',
            headers=headers,
            data=json.dumps(login2fa_payload),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_register(self):
        """Test case for user_register

        Register a new user inside the system
        """
        register_user_payload = {"favouriteDish":"Pizza","firstName":"John","lastName":"Smith","emailAddress":"john.smith@delicious.com","password":"test","birthDate":"1977-01-21T00:00:00.000+00:00","enableTwoFactor":True}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MAGLIANIM_1/oauth-pwd/1.0.0/auth/register',
            method='POST',
            headers=headers,
            data=json.dumps(register_user_payload),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
