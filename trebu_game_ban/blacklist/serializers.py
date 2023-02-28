from rest_framework import serializers
from .models import Blacklist, Game, Reason
import re


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

    def validate(self, name):
        if name == "" or name == " ":
            raise serializers.ValidationError("name could not be empty")
        return name


def validate_game(id_game):
    if not Game.objects.filter(id=id_game.pk).exists():
        raise serializers.ValidationError('The game doesn\'t exist, please check it.')


def validate_email_address(email):
    if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
        raise serializers.ValidationError('the email format is incorrect, please check it.')
    return email


def validate_reason(reason):
    reason = Reason.objects.get(reason=reason)
    print("REASOOOONS" + reason)
    if not Reason.objects.filter(reason=reason).exists():
        raise serializers.ValidationError('the reason doesn\'t exist, please check it.')


class BlackListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    class Meta:
        model = Blacklist
        fields = '__all__'

    def validate(self, data):
        return validate_email_address(data['email'])


