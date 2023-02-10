from rest_framework import permissions


class IsOwnerReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение, позволяющее редактировать объект только владельцам.
    """

    def has_object_permission(self, request, view, obj):
        """
        Разрешения на чтение разрешены для любого запроса,
        поэтому мы всегда будем разрешать запросы GET, HEAD или OPTIONS
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        """Разрешения на запись разрешены только владельцу фрагмента."""
        return obj.owner == request.user
