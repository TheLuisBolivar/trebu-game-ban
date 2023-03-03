from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.games.models import Game
from apps.games.api.serializers import GameSerializer


@api_view(['POST'])
def game_api_view_post(request):

    if request.method == 'POST':
        game_serializers = GameSerializer(data=request.data)

        if game_serializers.is_valid():
            game_serializers.save()
            return Response(status=200, data=game_serializers.data)
        return Response(status=400, data=game_serializers.errors)
    return Response(status=400)


@api_view(['GET'])
def game_api_view_get(request):

    if request.method == 'GET':
        games = Game.objects.all()
        game_serializers = GameSerializer(data=games, many=True)
        return Response(status=200, data=game_serializers.data)
    return Response(status=400)
