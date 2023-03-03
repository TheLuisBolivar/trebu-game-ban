from rest_framework import serializers
from apps.reasons.models import Reason


class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = '__all__'
