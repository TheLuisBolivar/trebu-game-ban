import re
from abc import ABC

from rest_framework import serializers
from .models import Blacklist, Game, Reason
from django.utils import timezone
from .dtos_rs import CheckBanInfoRsDto


class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = '__all__'


class BlackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        fields = ['email', 'game', 'reason']
        depth = 1

    def create(self, validated_data):
        data = dict(validated_data['data'])
        game = Game.objects.get(pk=data['game'])
        reason = Reason.objects.get(name=data['reason'])
        time = timezone.now()
        Blacklist.objects.create(email=data['email'], game=game, reason=reason, is_active=True, \
                                 date_report=time)
        return validated_data


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


def validate_email_format(email):
    result = True
    if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
        result = False
    return result


def is_email_exists(email):
    result = True
    if not Blacklist.objects.filter(email=email).exists():
        return False
    return result


class EmailValidator:
    @staticmethod
    def validate_email(email):
        return validate_email_format(email) & is_email_exists(email)