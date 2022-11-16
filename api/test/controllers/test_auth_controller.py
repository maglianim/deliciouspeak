from api.test.config.BaseTest import BaseTest
from flask import json
from mock import patch
from api.models.auth_login200_response import AuthLogin200Response
from api.biz.utils import jwt

class TestAuthController(BaseTest):
    base_path = 'http://127.0.0.1:5000/api/auth/{suffix}'

    def test_echo(self):
        input_message = 'input_message_example'
        query_string = [('input_message', input_message)]
        headers = { 
            'Accept': 'text/plain',
        }
        response = self.client.open(
            self.base_path.format(suffix='echo'),
            method='GET',
            headers=headers,
            query_string=query_string)
        assert response.data.decode('utf-8') == input_message
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_register_201(self):
        """Test case for user_register

        Register successfuly a new user inside the system
        """
        register_user_payload = self.__base_user_creation()

        response = self.__call_register_user(register_user_payload)

        self.assertStatus(response, 201, 'Response body is : ' + response.data.decode('utf-8'))        

    def test_register_400_bad_username(self):
        """Test case for user_register
        Testing data correctenss: if an invalid email address is provided, json schema validation should fail
        """
        register_user_payload = self.__base_user_creation()
        register_user_payload['emailAddress'] = 'definitely_not_a_mail_address'
        
        response = self.__call_register_user(register_user_payload)
        self.assert400(response,'Response body is : ' + response.data.decode('utf-8'))        

    def test_register_400_invalid_password(self):
        """Test case for user_register
        Testing data correctenss: if an invalid password is provided, json schema validation should fail (in this case too short pwd provided)
        """
        too_short_password = 'a'
        register_user_payload = self.__base_user_creation()
        register_user_payload['password'] = too_short_password

        response = self.__call_register_user(register_user_payload)

        self.assert400(response,'Response body is : ' + response.data.decode('utf-8'))        

    def test_register_409(self):
        """Test case for user_register
        Testing idempotence. The test tries to register twice the same user, expecting 409 status response in the second execution
        """
        register_user_payload = self.__base_user_creation()
        
        response = self.__call_register_user(register_user_payload)
        self.assertStatus(response, 201, 'Response body is : ' + response.data.decode('utf-8'))        

        response = self.__call_register_user(register_user_payload)
        self.assertStatus(response, 409, 'Response body is : ' + response.data.decode('utf-8'))        

    def test_login_401_invalid_request(self):
        """Test case for user_register
        Testing login with an invalid payload should break schema validation
        """
        login_payload = {"password":"not-existing"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            self.base_path.format(suffix='login'),
            method='POST',
            headers=headers,
            data=json.dumps(login_payload),
            content_type='application/json')
        self.assert400(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_login_401_invalid_credential(self):
        """Test case for user_register
        Testing login with a nonexistent user_name and password
        """

        response = self.__call_login(username='not.existing@deliciouspeak.com', password='not-existing')

        self.assert401(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_login_200_user_single_factor(self):
        """Test case for user_register
        Test create a user with single factor auth, then tries to login
        Expects 200 status code and a valid token as result
        """

        register_user_payload = self.__base_user_creation(enable_two_factor=False)
        response = self.__call_register_user(register_user_payload)
        response = self.__call_login(username=register_user_payload['emailAddress'], password=register_user_payload['password'])
        
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))
        
        resp_parsed = AuthLogin200Response.from_dict(json.loads(response.data.decode('utf-8')))
        self.__validate_auth_login_200_response(response = resp_parsed, expected_user_name=register_user_payload['emailAddress'])

    @patch('api.biz.auth.services.AuthService.MailService')
    def test_login_200_user_two_factor(self, mock_mail_service):
        """Test case for user_register
        Test create a user with two factor auth, then tries to login
        Expects:
        - 200 status code
        - empty response body
        - shipping of an otp to given email
        """

        register_user_payload = self.__base_user_creation(enable_two_factor=True)
        response = self.__call_register_user(register_user_payload)
        response = self.__call_login(username=register_user_payload['emailAddress'], password=register_user_payload['password'])
        
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))
        assert not response.data
        assert mock_mail_service.return_value.send.called

        mail_send_dict = self.__get_mail_service_call_dict(mock_mail_service.return_value.send)
        assert mail_send_dict['recipient'] == register_user_payload['emailAddress']

    @patch('api.biz.auth.services.AuthService.MailService')
    def test_login2fa_200(self, mock_mail_service):
        """Test case for user_register
        After calling login, perform login2fa to test the validity of generated otp
        Expects:
        - 200 status code
        - a valid token as result       
        """

        register_user_payload = self.__base_user_creation(enable_two_factor=True)
        response = self.__call_register_user(register_user_payload)
        response = self.__call_login(username=register_user_payload['emailAddress'], password=register_user_payload['password'])
        mail_send_dict = self.__get_mail_service_call_dict(mock_mail_service.return_value.send)
        response = self.__call_login2fa(username=register_user_payload['emailAddress'], otp=mail_send_dict['body'])

        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))
        resp_parsed = AuthLogin200Response.from_dict(json.loads(response.data.decode('utf-8')))
        self.__validate_auth_login_200_response(response = resp_parsed, expected_user_name=register_user_payload['emailAddress'])

    @patch('api.biz.auth.services.AuthService.MailService')
    def test_login2fa_401_same_otp_used_twice(self, mock_mail_service):
        """Test case for user_register
        Performs twice login2fa with same otp to check that it is not valid anymore
        Expects:
        - 401 status code
        """

        register_user_payload = self.__base_user_creation(enable_two_factor=True)
        response = self.__call_register_user(register_user_payload)
        response = self.__call_login(username=register_user_payload['emailAddress'], password=register_user_payload['password'])
        mail_send_dict = self.__get_mail_service_call_dict(mock_mail_service.return_value.send)

        response = self.__call_login2fa(username=register_user_payload['emailAddress'], otp=mail_send_dict['body'])
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

        response = self.__call_login2fa(username=register_user_payload['emailAddress'], otp=mail_send_dict['body'])
        self.assert401(response, 'Response body is : ' + response.data.decode('utf-8'))

    @patch('api.biz.auth.services.AuthService.MailService')
    def test_login2fa_401_first_otp_invalidated_by_other_login(self, mock_mail_service):
        """Test case for user_register
        Reproduce the following use case:
        - performs login and gets the generated otp
        - performs login again
        - test that the otp generated with the first login should be invalidated
        Expects:
        - 401 status code
        """

        register_user_payload = self.__base_user_creation(enable_two_factor=True)
        response = self.__call_register_user(register_user_payload)
        response = self.__call_login(username=register_user_payload['emailAddress'], password=register_user_payload['password'])
        mail_send_dict = self.__get_mail_service_call_dict(mock_mail_service.return_value.send)
        response = self.__call_login(username=register_user_payload['emailAddress'], password=register_user_payload['password'])
        
        response = self.__call_login2fa(username=register_user_payload['emailAddress'], otp=mail_send_dict['body'])
        self.assert401(response, 'Response body is : ' + response.data.decode('utf-8'))

    @patch('api.biz.auth.services.AuthService.MailService')
    def test_login2fa_401_correct_otp_provided_with_wrong_user_name(self, mock_mail_service):
        """Test case for user_register
        Reproduce the case when a login2fa is performed with an incorrect user.
        Expects:
        - 401 status code
        - Invalidation of otp
        """

        register_user_payload = self.__base_user_creation(enable_two_factor=True)
        response = self.__call_register_user(register_user_payload)
        response = self.__call_login(username=register_user_payload['emailAddress'], password=register_user_payload['password'])
        mail_send_dict = self.__get_mail_service_call_dict(mock_mail_service.return_value.send)

        response = self.__call_login2fa(username='oops_this_is_a_wrong@user.name', otp=mail_send_dict['body'])
        self.assert401(response, 'Response body is : ' + response.data.decode('utf-8'))

        response = self.__call_login2fa(username=register_user_payload['emailAddress'], otp=mail_send_dict['body'])
        self.assert401(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_login2fa_401_wrong_otp_provided(self):
        """Test case for user_register
        Reproduce the case when a login2fa is performed with an incorrect otp.
        Expects:
        - 401 status code
        """

        register_user_payload = self.__base_user_creation(enable_two_factor=True)
        response = self.__call_register_user(register_user_payload)
        response = self.__call_login(username=register_user_payload['emailAddress'], password=register_user_payload['password'])

        response = self.__call_login2fa(username=register_user_payload['emailAddress'], otp="wrong_otp")
        self.assert401(response, 'Response body is : ' + response.data.decode('utf-8'))
        

    def test_private_200_with_valid_token(self):
        """Test case for user_register
        Reproduce the authorized access to a private resource (a valid token is supplied)
        Expects:
        - 200 status code
        """

        register_user_payload = self.__base_user_creation(enable_two_factor=False)
        response = self.__call_register_user(register_user_payload)
        response = self.__call_login(username=register_user_payload['emailAddress'], password=register_user_payload['password'])
        resp_parsed = AuthLogin200Response.from_dict(json.loads(response.data.decode('utf-8')))
        response = self.__call_private(token=resp_parsed.token)
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))
        assert response.data.decode('utf-8') == 'Pizza with ananas is evil!'

    def test_private_401_with_no_token(self):
        """Test case for user_register
        Reproduce the unauthorized access to a private resource (no token is supplied)
        Expects:
        - 401 status code
        """

        response = self.__call_private(token=None)
        self.assert401(response, 'Response body is : ' + response.data.decode('utf-8'))        

    def test_private_401_with_expired_token(self):
        """Test case for user_register
        Reproduce the unauthorized access to a private resource (no token is supplied)
        Expects:
        - 401 status code
        """
        expired_token = jwt.generate_token('test@deliciouspeak.com', lifetime_seconds=-300)
        response = self.__call_private(token=expired_token)
        self.assert401(response, 'Response body is : ' + response.data.decode('utf-8'))        


    # region internal method
    
    def __call_register_user(self, register_user_payload):
        headers = { 
            'Content-Type': 'application/json',
        }
        return self.client.open(
            self.base_path.format(suffix='register'),
            method='POST',
            headers=headers,
            data=json.dumps(register_user_payload),
            content_type='application/json')
    
    def __call_login(self, username: str, password: str):
        login_payload = {"password": password,"username": username}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        return self.client.open(
            self.base_path.format(suffix='login'),
            method='POST',
            headers=headers,
            data=json.dumps(login_payload),
            content_type='application/json')
    
    def __call_login2fa(self, username: str, otp: str):
        login_payload = { "otp": otp, "username": username }
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        return self.client.open(
            self.base_path.format(suffix='login2fa'),
            method='POST',
            headers=headers,
            data=json.dumps(login_payload),
            content_type='application/json')

    def __call_private(self, token: str = None):
        headers = { 
            'Accept': 'application/json',
        }
        if token:
            headers['Authorization'] = 'Bearer {token}'.format(token=token)            
        return self.client.open(
            self.base_path.format(suffix='private'),
            method='GET',
            headers=headers)

    def __get_mail_service_call_dict(self, send_fn = None):
        if not send_fn:
            return None
        raw_args = send_fn.mock_calls[0][1]
        return { 
            'recipient': raw_args[0],
            'subject': raw_args[1],
            'body': raw_args[2],
        }

    def __base_user_creation(self, enable_two_factor=False):
        return {
            "favouriteDish":"Pizza",
            "firstName":"John",
            "lastName":"Smith",
            "emailAddress":"john.smith@delicious.com",
            "password":"long-enough-password",
            "birthDate":"1977-01-21T00:00:00.000+00:00",
            "enableTwoFactor":enable_two_factor
        }

    def __validate_auth_login_200_response(self, response: AuthLogin200Response, expected_user_name: str):        
        assert response.token
        
        decoded_token = jwt.decode_token(response.token)
        assert decoded_token['sub'] == expected_user_name


    # endregion internal method        
