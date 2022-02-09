from django.urls import path
from app_users.views import ArticlesList


urlpatterns = [
    path('articles/', ArticlesList.as_view(), name='articles_list')
]

