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

    def create(self, validated_data):
        groups = []

        if self.context.pop('author', False):
            groups.append(Group.objects.get(name='authors'))
            groups.append(Group.objects.get(name='subscribers'))

        elif self.context.pop('subscriber', False):
            groups.append(Group.objects.get(name='subscribers'))

        user = User.objects.create_user(**validated_data)
        user.groups.set(groups)
        return user


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ['title', 'text', 'author', 'creation_date', 'is_private']

    def create(self, validated_data):
        validated_data['author'] = self.context['author']
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.text = validated_data.get('text')
        instance.is_private = validated_data.get('is_private')
        instance.save(update_fields=validated_data.keys())
        return instance
