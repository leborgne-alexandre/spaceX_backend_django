from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import SpaceXSerializer      
from .models import SpaceX


class SpaceXView(viewsets.ModelViewSet):       
  serializer_class = SpaceXSerializer          
  queryset = SpaceX.objects.all()  