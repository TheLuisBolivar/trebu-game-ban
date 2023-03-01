from datetime import timedelta

from django.db.models import QuerySet
from rest_framework.decorators import api_view
from rest_framework.views import Response
from .serializers import BlackListSerializer, GameSerializer, EmailValidator
from .models import Blacklist
from django.utils import timezone
from .dtos_rs import CheckBanInfoRsDto


@api_view(['GET'])
def getInfoBlackList(rq, email):
    if not EmailValidator.validate_email(email):
        return Response(status=400, data="{message: \" Error in format or email does not exits, check it\"}")
    ban_info = getInfoByEmail(email)
    return Response(status=200, data=ban_info)


def get_reason_commonly_reported(crude_data):
    crude_data.group_by = ['reason']
    results = QuerySet(query=crude_data, model=Blacklist)
    print("get_reason_commonly_reported" + str(results))
    return "reason"


def get_number_times_reported(crude_data):
    return len(crude_data)


def get_number_games_reported(crude_data):
    crude_data.group_by = ['game']
    results = QuerySet(query=crude_data, model=Blacklist)
    return len(results)


def getInfoByEmail(email):
    crude_data = get_crude_data(email)
    return CheckBanInfoRsDto(get_reason_commonly_reported(crude_data),
                             get_number_times_reported(crude_data),
                             get_number_games_reported(crude_data))


def get_crude_data(email):
    this_week = timezone.now() - timedelta(days=90)
    return Blacklist.objects.filter(email=email).filter(date_report__gte=this_week).query()


@api_view(['POST'])
def postBlacklist(rq):
    seria = BlackListSerializer(data=rq.data)
    if not seria.is_valid():
        return Response(status=400, data=seria.errors)

    bl = seria.save(data=rq.data)
    return Response(status=200, data=bl)


@api_view(['POST'])
def create_game(rq):
    seria = GameSerializer(data=rq.data, context=rq.data)

    if not seria.is_valid():
        return Response(status=400, data=seria.errors)

    seria.save()
    return Response(status=202, data=seria.data)
