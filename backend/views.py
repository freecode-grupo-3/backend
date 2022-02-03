from django.shortcuts import render
from rest_framework import viewsets, filters

from backend.models import Disease, Reference, ReferenceType
from backend.serializers import DiseaseSerializer, ReferenceSerializer, ReferenceTypeSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class ReferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ReferenceSerializer
    queryset = Reference.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class DiseaseViewSet(viewsets.ModelViewSet):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all()
    permission_classes = (AllowAny,)


class ReferenceTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ReferenceTypeSerializer
    queryset = ReferenceType.objects.all()
    permission_classes = (AllowAny,)
