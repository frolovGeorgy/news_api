import logging

from django.contrib.auth import logout, authenticate, login
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from app_users.models import Article, User
from app_users.permissions import AuthorPermission
from app_users.serializers import ArticleSerializer, UserSerializer

logger = logging.getLogger()
logger.setLevel('INFO')


# TODO удалить, это для проверки
class ExampleView(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
            'id': str(request.user.id),
            'is_authenticated': str(request.user.is_authenticated),
            'groups': str(request.user.groups.all()),
            'permissions': str(request.user.get_user_permissions())
        }
        return Response(content)


class LoginView(APIView):

    def post(self, request):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(
            data=data,
            context={
                'author': data.get('author', False),
                'subscriber': data.get('subscriber', False)
            }
        )

        if serializer.is_valid():
            self.perform_create(serializer)
            email = data.get('email', None)
            password = data.get('password', None)
            user = authenticate(username=email, password=password)
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class LogoutView(APIView):

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class ArticlesListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        if self.request.user.has_perm('app_users.can_view_privates'):
            return Article.objects.all()
        return Article.objects.filter(is_private=False)


class AddArticleView(CreateAPIView):
    permission_classes = [AuthorPermission]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        context = {'author': request.user}
        serializer = self.get_serializer(
            data=data,
            context=context
        )

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
