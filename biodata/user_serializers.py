from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class AdminRegistrationSerializer(RegisterSerializer):
    """
    Custom serializer for admin registration.
    Sets the new user's is_staff status to True.
    """
    def save(self, request):
        user = super().save(request)
        user.is_staff = True
        user.save()
        return user