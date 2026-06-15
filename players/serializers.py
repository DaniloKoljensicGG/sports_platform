from rest_framework import serializers
from .models import PlayerProfile, Sport


class PlayerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = "__all__"

    # def age(self, ):
    #     today =


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"
