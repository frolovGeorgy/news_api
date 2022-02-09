from rest_framework import serializers

from .models import Article, Author


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ['title', 'text', 'author', 'creation_date', 'is_private']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
