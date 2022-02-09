from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from app_users.managers import MyUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email


class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=True)


class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/sas/"
