from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import PlayerProfile, Sport
from .serializers import PlayerProfileSerializer, SportSerializer

# Create your views here.


class PlayerProfileViewSet(ModelViewSet):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer


class SportViewSet(ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
