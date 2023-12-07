from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Article, Journalist
from .serializers import ArticleSerializer, JournalistSerializer


class JournalistListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        authors = Journalist.objects.all()
        serializer = JournalistSerializer(
            authors, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        article = get_object_or_404(Article, id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        article = get_object_or_404(Article, id=pk)
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        article = get_object_or_404(Article, id=pk)
        article.delete()
        return Response(
            {
                "process": {
                    "code": 204,
                    "message": f"Article whose id was {pk} has been deleted",
                }
            },
            status=status.HTTP_204_NO_CONTENT,
        )
