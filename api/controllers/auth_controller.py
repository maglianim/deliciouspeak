"""
    Auth controller - TODO
"""
from http import HTTPStatus
import connexion
from api.biz.core.models.exceptions import *
from api.biz.auth.services.AuthService import AuthService
from api.biz.user.services.UserService import UserService
from api.models.auth_login200_response import AuthLogin200Response  # noqa: E501
from api.models import mappers
from api.models.login_payload import LoginPayload  # noqa: E501
from api.models.login_success_resp import LoginSuccessResp  # noqa: E501
from api.models.login2fa_payload import Login2faPayload  # noqa: E501
from api.models.register_user_payload import RegisterUserPayload  # noqa: E501


def auth_login(login_payload=None):  # noqa: E501
    """Logs a user inside the system

    After receiving username and password, the system checks the validity and behaves depending on the authentication type configured during the signup process. - correct credentials with single factor login: an auth jwt token is issued - correct credentials with two factor login: an OTP is sent to the provided user email address - incorrect credentials: unauthorized response is provided regardless of the type of authentication  # noqa: E501

    :param login_payload: Login credentials
    :type login_payload: dict | bytes

    :rtype: Union[AuthLogin200Response, Tuple[AuthLogin200Response, int], Tuple[AuthLogin200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        login_payload = LoginPayload.from_dict(connexion.request.get_json())  # noqa: E501
        service = AuthService()
        login_result = service.login(login_payload.username, login_payload.password)
        print(login_result)
        if not login_result[0]:
            return None, HTTPStatus.UNAUTHORIZED
        if not login_result[1]:
            return None, HTTPStatus.OK        
        return AuthLogin200Response(token = login_result[1]), HTTPStatus.OK


def auth_login2fa_post(login2fa_payload=None):  # noqa: E501
    """performs two factor login

    The system check if the otp (previously sent to user-provided email) is valid  # noqa: E501

    :param login2fa_payload: two factord Login credentials
    :type login2fa_payload: dict | bytes

    :rtype: Union[LoginSuccessResp, Tuple[LoginSuccessResp, int], Tuple[LoginSuccessResp, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        login2fa_payload = Login2faPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_register(register_user_payload=None):  # noqa: E501
    """Register a new user inside the system

    Validates and adds a new user as a result of a registration process # noqa: E501

    :param register_user_payload: 
    :type register_user_payload: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        register_user_payload = RegisterUserPayload.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            user_service = UserService()
            user_service.create(mappers.from_register_userpayload_to_user(register_user_payload))
            return None, HTTPStatus.CREATED
        except ResourceExistingException:
            return None, HTTPStatus.CONFLICT
        except Exception:
            return None, HTTPStatus.BAD_REQUEST
