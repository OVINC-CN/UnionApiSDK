from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from ovinc_client.account.models import User

USER_MODEL: User = get_user_model()


class UserSignInSerializer(Serializer):
    """
    Sign In
    """

    code = serializers.CharField(label=gettext_lazy("Code"))


class UserInfoSerializer(ModelSerializer):
    """
    User Info
    """

    class Meta:
        model = USER_MODEL
        fields = ["username", "nick_name", "user_type", "last_login"]
