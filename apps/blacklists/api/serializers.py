from rest_framework import serializers
from apps.blacklists.models import Blacklist


class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        fields = ['game', 'reason', 'email']
