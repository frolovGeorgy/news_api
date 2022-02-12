from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.has_perm('app_users.can_create_articles')
