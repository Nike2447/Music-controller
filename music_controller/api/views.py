from .models import Room
from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer

# Create your views here.


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
