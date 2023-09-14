from typing import Tuple, Union

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from rest_framework.authentication import SessionAuthentication

from ovinc_client import OVINCClient
from ovinc_client.constants import ResponseData
from ovinc_client.core.exceptions import LoginRequired
from ovinc_client.core.logger import logger

USER_MODEL = get_user_model()


class SessionAuthenticate(SessionAuthentication):
    """
    Session Auth
    """

    def authenticate(self, request) -> Union[Tuple[USER_MODEL, None], None]:
        user = getattr(request._request, "user", None)  # pylint: disable=W0212
        if user is None or not user.is_active:
            return None
        return user, None


class LoginRequiredAuthenticate(SessionAuthenticate):
    """
    Login Required Authenticate
    """

    def authenticate(self, request) -> (USER_MODEL, None):
        user = super().authenticate(request)
        if user is None or not user[0].is_active:
            raise LoginRequired()
        return user


class OAuthBackend(BaseBackend):
    """
    OAuth
    """

    # pylint: disable=R1710
    def authenticate(self, request, code: str = None, **kwargs):
        if not code:
            return
        # Union API Auth
        try:
            # Request
            client = OVINCClient(
                app_code=settings.APP_CODE, app_secret=settings.APP_SECRET, union_api_url=settings.OVINC_API_DOMAIN
            )
            resp: ResponseData = client.auth.verify_code({"code": code})
            data: dict = resp.data.get("data", {})
            if data and data.get("username"):
                username = data["username"]
                user = USER_MODEL.objects.get_or_create(username=username)[0]
                for key, val in data.items():
                    setattr(user, key, val)
                user.save(update_fields=data.keys())
                return user
            logger.info("[UnionAuthFailed] Result => %s", resp.data)
            return None
        except Exception as err:  # pylint: disable=W0718
            logger.exception(err)
            return None
