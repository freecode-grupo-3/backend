from rest_framework import serializers
from .models import Disease, Reference, ReferenceType

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = serializers.ALL_FIELDS

class ReferenceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceType
        fields = serializers.ALL_FIELDS


class ReferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reference
        read_only_fields = ['created_at', 'last_modified', 'created_by']
