from django.urls import path

from app_users.views import (ArticlesListView, LoginView, LogoutView, RegistrationView, AddArticleView,
                             UpdateArticleView, DeleteArticleView)

urlpatterns = [
    path('articles/', ArticlesListView.as_view(), name='articles_list'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('add_article/', AddArticleView.as_view(), name='add_article'),
    path('update_article/<int:id>', UpdateArticleView.as_view(), name='update_article'),
    path('delete_article/<int:id>', DeleteArticleView.as_view(), name='delete_article'),
]
