from rest_framework import viewsets
from applications.games.models import Game
from applications.api.v1.serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer