from django.contrib import admin

from app_users.models import Article, Author, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author', 'creation_date', 'is_private']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
