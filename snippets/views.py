from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerReadOnly
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions


class SnippetList(generics.ListCreateAPIView):
    """
    Выводит все фрагменты кода или создаёт новый фрагмент
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Получает, обновляет, удаляет фрагмент кода
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly]


class UserList(generics.ListAPIView):
    """
    Выводит всех пользователей или создаёт нового
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Получить пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
