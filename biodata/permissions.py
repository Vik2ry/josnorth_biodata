from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users (staff) to edit an object.
    Read-only access is allowed for any user (authenticated or not).
    """

    def has_permission(self, request, view):
        # Allow read-only methods for any request.
        if request.method in permissions.SAFE_METHODS:
            return True

        # For write methods, only allow if the user is an admin.
        return request.user and request.user.is_staff