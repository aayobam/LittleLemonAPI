from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow superusers and users with admin role to perform any action
        return request.user.is_superuser or request.user.groups.filter(name__iexact='admin').exists()


class ManagerPermission(permissions.BasePermission):
    methods = ['POST', 'PUT', 'PATCH', 'GET', 'DELETE']
    message = "Only managers and superusers can perform this operation."

    def has_permission(self, request, view):
        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True
        
        # Only allow managers to add and remove users from groups
        elif request.user.groups.filter(name__iexact='manager').exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True
        # Only allow managers to delete users from groups
        elif request.method in self.methods:
            return True
        return False
    

class DeliveryCrewPermission(permissions.BasePermission):
    methods = ['PUT', 'PATCH', 'GET']
    message = "only superusers, managers and delivery crew can perform this operation."

    def has_permission(self, request, view):
        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Allow superusers to perform any action on any object.
        if request.user.is_superuser:
            return True
        # Only allow delivery crew to update delivery status of an order they are assigned to
        elif request.user.groups.filter(name__iexact='delivery crew').exists():
            return obj.delivery_crew == request.user and request.method in self.methods
        return False
    