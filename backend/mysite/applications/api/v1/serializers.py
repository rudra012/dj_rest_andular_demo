from rest_framework.serializers import ModelSerializer
from applications.games.models import Game


class GameSerializer(ModelSerializer):

    class Meta:
        model = Game