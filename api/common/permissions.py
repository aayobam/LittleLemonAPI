from rest_framework import permissions


class SuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow superusers and users with admin role to perform any action
        return bool(request.user and request.user.is_superuser)


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
    message = "Only delivery crew can perform this operation."

    def has_permission(self, request, view):
        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True
        
        # Only allow managers to add and remove users from groups
        elif request.user.groups.filter(name__iexact='delivery crew').exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True
        # Only allow managers to delete users from groups
        if request.method in self.methods:
            return True
        return obj.delivery_crew == request.user
        #return False


class IsOwnerPermission(permissions.BasePermission):
    message = "Only owner or superuser can perform this operation"
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.user == request.user
