from django.contrib.auth import logout, authenticate, login
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from app_users.models import Article
from app_users.serializers import ArticleSerializer


class ExampleView(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
            'is_authenticated': str(request.user.is_authenticated)
        }
        return Response(content)


class LoginView(APIView):

    def post(self, request):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class ArticlesList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        # TODO изменить проверку аутентификации
        if self.request.user.is_authenticated:
            return Article.objects.all()
        return Article.objects.filter(is_private=False)
