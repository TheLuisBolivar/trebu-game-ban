from rest_framework import serializers
from .models import Blacklist, Game, Reason
from django.utils import timezone


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
