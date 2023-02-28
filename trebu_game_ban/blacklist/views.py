from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import Response
from .serializers import BlackListSerializer, GameSerializer


@api_view(['GET'])
def getInfoBlackList(request):
    return HttpResponse("Esto es el get :D")


@api_view(['POST'])
def postBlacklist(rq):
    seria = BlackListSerializer(data=rq.data)
    if not seria.is_valid():
        return Response(status=400, data=seria.errors)
    return Response(status=200, data=seria.data)


@api_view(['POST'])
def create_game(rq):
    seria = GameSerializer(data=rq.data)

    if not seria.is_valid():
        return Response(status=400, data=seria.errors)

    seria.save()
    return Response(status=202, data=seria.data)
