from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from app_users.managers import MyUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        permissions = (
            ('can_view_privates', 'Can view private articles'),
            ('can_create_articles', 'Can create new articles'),
        )

    def __str__(self):
        return self.email


class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=True)
