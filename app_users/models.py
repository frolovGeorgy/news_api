from django.db import models


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
