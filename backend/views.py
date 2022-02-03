from django.shortcuts import render
from rest_framework import viewsets

from backend.models import Reference
from backend.serializers import ReferenceSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class ReferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ReferenceSerializer
    queryset = Reference.objects.all()
    permission_classes = (IsAuthenticated,)

