from django.contrib import admin
from django.forms import ModelForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from app_users.models import Article, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author', 'creation_date', 'is_private']


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        password = self.cleaned_data.get('password')
        if password:
            try:
                validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password', error)
