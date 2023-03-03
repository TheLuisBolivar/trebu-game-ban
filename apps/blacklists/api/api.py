from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.blacklists.models import Blacklist
from apps.blacklists.api.serializers import BlacklistSerializer


@api_view(['GET'])
def blacklist_api_view_get(request):
    if request.method == 'GET':
        blacklists = Blacklist.objects.all()
        blacklists_serializers = BlacklistSerializer(data=blacklists, many=True)
        return Response(status=200, data=blacklists_serializers.data)
    return Response(status=400)


@api_view(['POST'])
def blacklist_api_view_post(request):

    if request.method == 'POST':
        blacklists_serializers = BlacklistSerializer(data=request.data)

        if blacklists_serializers.is_valid():
            blacklists_serializers.save()
            return Response(status=200, data=blacklists_serializers.data)
        return Response(status=400, data=blacklists_serializers.errors)
    return Response(status=400)
