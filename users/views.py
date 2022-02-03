from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import User
from users.serializers import CreateUserSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    """
    User ViewSet
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @action( methods=["GET"], detail=False)
    def me(self, request):
        if request.user.id:
            serializer = UserSerializer(request.user, context={"request": request})
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

class CreateUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Create User ViewSet
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)
