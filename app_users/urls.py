from django.urls import path

from app_users.views import ArticlesListView, ExampleView, LoginView, LogoutView, RegistrationView, AddArticleView

urlpatterns = [
    path('articles/', ArticlesListView.as_view(), name='articles_list'),
    path('example/', ExampleView.as_view(), name='example'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('add_article/', AddArticleView.as_view(), name='add_article'),
]
