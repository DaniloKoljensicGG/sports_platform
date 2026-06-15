from rest_framework import serializers
from .models import PlayerProfile, Sport
from datetime import date


class PlayerProfileSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = PlayerProfile
        fields = "__all__"

    def get_age(self, obj):
        if not obj.date_of_birth:
            return None

        today = date.today()

        age = (
            today.year
            - obj.date_of_birth.year
            - (
                (today.month, today.day)
                < (obj.date_of_birth.month, obj.date_of_birth.day)
            )
        )
        return age


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"
