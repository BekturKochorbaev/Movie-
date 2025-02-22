from rest_framework import permissions


class CheckMovie(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == 'pro':
            return True

        if request.user.status == 'simple' and obj.status == 'pro':
            return False
        return True
