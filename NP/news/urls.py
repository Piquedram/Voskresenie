from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostsView.as_view(), name='posts_list'),
    path('posts/<int:pk>', PostView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

    path('news/', NewsView.as_view(), name='news_list'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),

    path('articles/', ArticlesView.as_view(), name='articles_list'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
]
