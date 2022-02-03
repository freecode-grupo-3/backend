from attr import validate
from rest_framework import serializers, exceptions
from django.contrib.auth.models import Group
from users.models import User
from backend.serializers import DiseaseSerializer, ReferenceTypeSerializer
from backend.models import Disease, ReferenceType

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = serializers.ALL_FIELDS

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    diseases_of_interest = DiseaseSerializer(many=True)
    reference_types_of_interest = ReferenceTypeSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','email', 'is_active', 'groups', 'diseases_of_interest', 'reference_types_of_interest')

class CreateUserSerializer(serializers.ModelSerializer):

    groups = serializers.CharField()

    def create(self, validated_data):
        try:
            groups = Group.objects.get(name = validated_data.pop('groups'))
        except Group.DoesNotExist:
            raise exceptions.NotFound("Grupo/Rol no Existe")

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

class UserWithDiseasesAndReferenceTypesSerializer(serializers.ModelSerializer):
    diseases_of_interest = serializers.ListField(child=serializers.CharField(), allow_empty=False, write_only=True)
    reference_types_of_interest = serializers.ListField(child=serializers.CharField(), allow_empty=False, write_only=True)

    def _handle_diseases(self, instance, disease_names):
        found_diseases = Disease.objects.filter(name__in=disease_names)
        if len(disease_names) > len(found_diseases):
            current_diseases = set([disease.name for disease in found_diseases])
            extra_names = set(disease_names) - current_diseases
            raise exceptions.ValidationError({'error': 'The following are extra disease names {}'.format(extra_names)})

        # TODO: Properly call .add and .remove to better use of ids
        instance.diseases_of_interest.set(found_diseases)

    def _handle_reference_types(self, instance, reference_type_names):
        found_ref_types = ReferenceType.objects.filter(name__in=reference_type_names)
        if len(reference_type_names) > len(found_ref_types):
            current_diseases = set([reference_type.name for reference_type in found_ref_types])
            extra_names = set(reference_type_names) - current_diseases
            raise exceptions.ValidationError({'error': 'The following are extra ref types names {}'.format(extra_names)})

        # TODO: Properly call .add and .remove to better use of ids
        instance.reference_types_of_interest.set(found_ref_types)



    def update(self, instance, validated_data):
        disease_names = set(validated_data.pop('diseases_of_interest'))
        reference_type_names = set(validated_data.pop('reference_types_of_interest'))

        self._handle_diseases(instance, disease_names)
        self._handle_reference_types(instance, reference_type_names)
        instance.save()

        return instance

    class Meta:
        model = User
        fields = ('diseases_of_interest', 'reference_types_of_interest')
