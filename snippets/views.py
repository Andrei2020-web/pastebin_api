from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerReadOnly
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User


class SnippetViewSet(viewsets.ModelViewSet):
    """
    Набор представлений автоматически предоставляет действия 'список',
    'создать', 'извлечь', 'обновить' и 'уничтожить' + дополнительное действие 'подсветка'.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Набор представлений автоматически предоставляет действия 'список', 'создать'
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
