from django.urls import path
from app_users.views import ArticlesList, ExampleView, LoginView, LogoutView, RegistrationAPIView


urlpatterns = [
    path('articles/', ArticlesList.as_view(), name='articles_list'),
    path('example/', ExampleView.as_view(), name='example'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationAPIView.as_view(), name='registration'),
]

