from rest_framework import serializers, exceptions
from django.contrib.auth.models import Group
from users.models import User

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = serializers.ALL_FIELDS

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','email', 'is_active', 'groups')


class CreateUserSerializer(serializers.ModelSerializer):

    groups = serializers.CharField()

    def create(self, validated_data):
        try:
            groups = Group.objects.get(name = validated_data.pop('groups'))
        except Group.DoesNotExist:
            raise exceptions.APIException("Grupo/Rol no Existe")

        user = User.objects.create_user(**validated_data)
        user.is_active = True
        user.set_password(validated_data.get('password'))
        user.groups.add(groups)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'groups')
        extra_kwargs = {'password': {'write_only': True}}