from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserIsOwnerAdventures(BasePermission):

    def has_object_permission(self, request, view, adventure):
        return request.user.id == adventure.user.id


class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'
    my_safe_method = ['GET', 'PUT']

    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user