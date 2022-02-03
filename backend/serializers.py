from rest_framework import serializers
from .models import Disease, ReferenceType

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = serializers.ALL_FIELDS

class ReferenceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceType
        fields = serializers.ALL_FIELDS
