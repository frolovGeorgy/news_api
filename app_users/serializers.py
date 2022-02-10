import logging

from django.contrib.auth.models import Group
from rest_framework import serializers

from app_users.models import Article, User

logger = logging.getLogger()
logger.setLevel('INFO')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, kwargs):
        groups = []

        if self.context.pop('author', False) is True:
            groups.append(Group.objects.get(name='authors'))

        elif self.context.pop('subscriber', False) is True:
            groups.append(Group.objects.get(name='subscribers'))

        user = User.objects.create_user(**kwargs)
        user.groups.set(groups)
        return user


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ['title', 'text', 'author', 'creation_date', 'is_private']
