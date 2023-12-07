from django.urls import path
from .views import *

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path(
        "articles/<int:pk>",
        ArticleDetailAPIView.as_view(),
        name="article-detail",
    ),
    path("authors/", JournalistListCreateAPIView.as_view(), name="author-list"),
]
