from rest_framework import serializers
from .models import CosmicObject

class CosmicObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CosmicObject
        fields = ['id', 'name', 'description', 'user']
