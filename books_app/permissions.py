from django.conf import settings
from rest_framework.permissions import BasePermission

from .jwt_helper import get_jwt_payload, get_access_token
from .models import CustomUser


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        access_token = get_access_token(request)

        if access_token is None:
            return False

        # Ensure token is valid
        try:
            payload = get_jwt_payload(access_token)
        except Exception as e:
            return False

        # Ensure user exists
        try:
            user = CustomUser.objects.get(pk=payload["user_id"])
        except Exception as e:
            return False

        return user.is_active


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        token = get_access_token(request)

        if token is None:
            return False

        # Ensure token is valid
        try:
            payload = get_jwt_payload(token)
        except Exception as e:
            return False

        # Ensure user exists
        try:
            user = CustomUser.objects.get(pk=payload["user_id"])
        except Exception as e:
            return False

        return user.is_moderator


class IsRemoteService(BasePermission):
    def has_permission(self, request, view):
        access_key = request.data.get("access_key", "")
        return access_key == 123
