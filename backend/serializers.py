from rest_framework import serializers
from .models import Enfermedad

class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = serializers.ALL_FIELDS