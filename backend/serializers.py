from rest_framework import serializers
from .models import Disease

class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = serializers.ALL_FIELDS