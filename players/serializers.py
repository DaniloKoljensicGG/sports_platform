from rest_framework import serializers
from .models import PlayerProfile, Sport


class PlayerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = [
            "first_name",
            "last_name",
            "primary_position",
            "height_cm",
            "weight_kg",
        ]
