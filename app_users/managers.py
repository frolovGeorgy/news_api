from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_values):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_values)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_values):
        extra_values.setdefault('is_staff', True)
        extra_values.setdefault('is_superuser', True)
        extra_values.setdefault('is_active', True)

        return self.create_user(email, password, **extra_values)
