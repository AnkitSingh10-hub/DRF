from django.urls import path
from .views import *

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path(
        "articles/<int:value_from_url>",
        ArticleDetailAPIView.as_view(),
        name="article-detail",
    ),
]
