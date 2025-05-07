# biblioteca/permissions.py

from rest_framework import permissions

class IsAuthenticated(permissions.BasePermission):
    """
    Permiso personalizado que permite el acceso solo a usuarios autenticados.
    """
    def has_permission(self, request, view):
        # Verifica si el usuario está autenticado
        return request.user and request.user.is_authenticated
