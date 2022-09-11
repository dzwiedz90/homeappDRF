from rest_framework import serializers

from .models import Treatment, Disease, MedicalTest, Clinic


class GetAllTreatmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ['id', 'treatment_name', 'description']


class CreateTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ['treatment_name', 'description']

        def save(self, instance, validated_data):
            instance.treatment_name = validated_data.get('treatment_name', instance.treatment_name)
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance


class UpdateTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ['treatment_name', 'description']

        def update(self, instance, validated_data):
            instance.treatment_name = validated_data.get('treatment_name', instance.treatment_name)
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance


class GetAllDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['id', 'disease_name', 'description']


class CreateDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['disease_name', 'description']

        def save(self, instance, validated_data):
            instance.disease_name = validated_data.get('disease_name', instance.disease_name)
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance


class UpdateDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['disease_name', 'description']

        def update(self, instance, validated_data):
            instance.disease_name = validated_data.get('disease_name', instance.disease_name)
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance


class GetAllMedicalTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTest
        fields = ['id', 'medical_test_name', 'description']


class CreateMedicalTesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTest
        fields = ['medical_test_name', 'description']

        def save(self, instance, validated_data):
            instance.medical_test_name = validated_data.get('medical_test_name', instance.medical_test_name)
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance


class UpdateMedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTest
        fields = ['medical_test_name', 'description']

        def update(self, instance, validated_data):
            instance.medical_test_name = validated_data.get('medical_test_name', instance.medical_test_name)
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance


class GetAllClinicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'clinic_name', 'address', 'phone_number', 'opening_hours']


class CreateClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['clinic_name', 'address', 'phone_number', 'opening_hours']

        def save(self, instance, validated_data):
            instance.clinic_name = validated_data.get('clinic_name', instance.clinic_name)
            instance.address = validated_data.get('address', instance.address)
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
            instance.opening_hours = validated_data.get('opening_hours', instance.opening_hours)
            instance.save()
            return instance


class UpdateClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['clinic_name', 'address', 'phone_number', 'opening_hours']

        def update(self, instance, validated_data):
            instance.clinic_name = validated_data.get('clinic_name', instance.clinic_name)
            instance.address = validated_data.get('address', instance.address)
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
            instance.opening_hours = validated_data.get('opening_hours', instance.opening_hours)
            instance.save()
            return instance
