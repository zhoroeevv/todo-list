from rest_framework import permissions

class UserPermissions(permissions.BasePermissions):
    def has_objeck_permissions(self, request, view, obj):
        return bool(obj.pk == request.user.pk)
    