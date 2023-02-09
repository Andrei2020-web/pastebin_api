from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics


class Snippet_list(generics.ListCreateAPIView):
    """
    Выводит все фрагменты кода или создаёт новый фрагмент
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class Snippet_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Получает, обновляет, удаляет фрагмент кода
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
