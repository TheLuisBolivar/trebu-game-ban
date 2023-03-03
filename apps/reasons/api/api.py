from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.reasons.models import Reason
from apps.reasons.api.serializers import ReasonSerializer


@api_view(['POST'])
def reason_api_view_post(request):

    if request.method == 'POST':
        reason_serializers = ReasonSerializer(data=request.data)

        if reason_serializers.is_valid():
            reason_serializers.save()
            return Response(status=200, data=reason_serializers.data)
        return Response(status=400, data=reason_serializers.errors)
    return Response(status=400)


@api_view(['GET'])
def reason_api_view_get(request):

    if request.method == 'GET':
        reasons = Reason.objects.all()
        reason_serializers = ReasonSerializer(reasons, many=True)
        return Response(status=200, data=reason_serializers.data)
    return Response(status=400)
