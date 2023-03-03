from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer


@api_view(['POST'])
def user_api_view_post(request):

    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(status=200, data=user_serializer.data)
        return Response(status=400, data=user_serializer.errors)
    return Response(status=400)


@api_view(['GET'])
def user_api_view_get(request):

    if request.method == 'GET':
        users = User.objects.all()
        user_serializers = UserSerializer(data=users, many=True)
        return Response(status=200, data=user_serializers.data)
    return Response(status=400)
