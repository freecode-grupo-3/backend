from rest_framework import serializers
from .models import Disease, DoctorReference, LabTestReference, MedicineReference, Reference, ReferenceType

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = serializers.ALL_FIELDS

class ReferenceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceType
        fields = serializers.ALL_FIELDS

common_reference_fields = ['created_at', 'last_modified', 'created_by', 'place_of_origin_name', 'address_of_place_of_origin', 'extra_info']

class MedicineReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineReference
        fields = common_reference_fields + ['name', 'presentation', 'price', 'currency']

class LabTestReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestReference
        fields = common_reference_fields + ['name', 'who_runs_the_test', 'price', 'currency']

class DoctorReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorReference
        fields = common_reference_fields + ['name', 'specialty', 'contact_phone_number', 'price', 'currency']

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = serializers.ALL_FIELDS
        read_only_fields = common_reference_fields

    def to_representation(self, instance):
        child = instance.child
        if isinstance(child, MedicineReference):
            return MedicineReferenceSerializer(instance=child).data
        if isinstance(child, DoctorReference):
            return DoctorReferenceSerializer(instance=child).data
        if isinstance(child, LabTestReference):
            return LabTestReferenceSerializer(instance=child).data
        return super().to_representation(instance=instance)
