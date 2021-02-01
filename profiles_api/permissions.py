from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''Allow users to edit their own profile'''

    def has_object_permission(self, request, view, obj):
        '''Chack user is editing their own profile'''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id