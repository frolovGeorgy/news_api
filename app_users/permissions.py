from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    message = 'Non-author not allowed to add an articles'

    def has_permission(self, request, view):
        return request.user.has_perm('app_users.can_create_articles')


class UpdateArticlePermission(permissions.BasePermission):
    message = 'Only article author allowed to update an article'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class DeleteArticlePermission(permissions.BasePermission):
    message = 'Only article author allowed to delete an article'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
