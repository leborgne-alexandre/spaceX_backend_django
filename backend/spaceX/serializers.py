from rest_framework import serializers
from .models import SpaceX

class SpaceXSerializer(serializers.ModelSerializer):
  class Meta:
    model = SpaceX
    fields = ('id', 'title', 'description')