from rest_framework import serializers

from .models import Human, HumanTreatment, HumanDisease, TreatmentUpdate, DiseaseUpdate, HumanMedicalTests, HumanWeight, \
    HumanGeneralInformation


class GetAllHumansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ['id', 'name', 'gender', 'date_born', 'height', 'current_weight', 'is_archived', 'photo']


class CreateHumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ['name', 'gender', 'date_born', 'height', 'current_weight', 'photo']

        def save(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.gender = validated_data.get('gender', instance.gender)
            instance.date_born = validated_data.get('date_born', instance.date_born)
            instance.height = validated_data.get('height', instance.height)
            instance.current_weight = validated_data.get('current_weight', instance.current_weight)
            instance.is_archived = validated_data.get('is_archived', instance.is_archived)
            instance.photo = validated_data.get('photo', instance.photo)
            instance.save()
            return instance


class UpdateHumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ['name', 'gender', 'date_born', 'height', 'current_weight', 'photo']

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.gender = validated_data.get('gender', instance.gender)
            instance.date_born = validated_data.get('date_born', instance.date_born)
            instance.height = validated_data.get('height', instance.height)
            instance.current_weight = validated_data.get('current_weight', instance.current_weight)
            instance.photo = validated_data.get('photo', instance.photo)
            instance.save()
            return instance


class GetAllHumansTreatmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanTreatment
        fields = ['id', 'human', 'treatment', 'clinic', 'date_occurred', 'date_treated', 'description', 'satisfaction',
                  'doctor']


class CreateHumanTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanTreatment
        fields = ['human', 'treatment', 'clinic', 'date_occurred', 'description', 'satisfaction',
                  'doctor']

        def save(self, instance, validated_data):
            instance.human = validated_data.get('human', instance.human)
            instance.treatment = validated_data.get('treatment', instance.treatment)
            instance.clinic = validated_data.get('clinic', instance.clinic)
            instance.date_occurred = validated_data.get('date_occurred', instance.date_occurred)
            instance.description = validated_data.get('description', instance.description)
            instance.satisfaction = validated_data.get('satisfaction', instance.satisfaction)
            instance.doctor = validated_data.get('doctor', instance.doctor)
            instance.save()
            return instance


class UpdateHumanTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanTreatment
        fields = ['human', 'treatment', 'clinic', 'date_occurred', 'date_treated', 'description', 'satisfaction',
                  'doctor']

        def update(self, instance, validated_data):
            instance.human = validated_data.get('human', instance.human)
            instance.treatment = validated_data.get('treatment', instance.treatment)
            instance.clinic = validated_data.get('clinic', instance.clinic)
            instance.date_occurred = validated_data.get('date_occurred', instance.date_occurred)
            instance.date_treated = validated_data.get('date_treated', instance.date_treated)
            instance.description = validated_data.get('description', instance.description)
            instance.satisfaction = validated_data.get('satisfaction', instance.satisfaction)
            instance.doctor = validated_data.get('doctor', instance.doctor)
            instance.save()
            return instance


class GetAllHumanTreatmentUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentUpdate
        fields = ['id', 'treatment_update', 'human_treatment']


class CreateHumanTreatmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentUpdate
        fields = ['treatment_update', 'human_treatment']

        def save(self, instance, validated_data):
            instance.treatment_update = validated_data.get('treatment_update', instance.treatment_update)
            instance.treatment = validated_data.get('treatment', instance.treatment)
            instance.save()
            return instance


class UpdateHumanTreatmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentUpdate
        fields = ['treatment_update', 'human_treatment']

        def update(self, instance, validated_data):
            instance.treatment_update = validated_data.get('treatment_update', instance.treatment_update)
            instance.treatment = validated_data.get('treatment', instance.treatment)
            instance.save()
            return instance


class GetAllHumansDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanDisease
        fields = ['id', 'human', 'disease', 'clinic', 'date_occurred', 'date_treated', 'description', 'satisfaction',
                  'doctor']


class CreateHumanDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanDisease
        fields = ['human', 'disease', 'clinic', 'date_occurred', 'description', 'satisfaction',
                  'doctor']

        def save(self, instance, validated_data):
            instance.human = validated_data.get('human', instance.human)
            instance.disease = validated_data.get('disease', instance.disease)
            instance.clinic = validated_data.get('clinic', instance.clinic)
            instance.date_occurred = validated_data.get('date_occurred', instance.date_occurred)
            instance.description = validated_data.get('description', instance.description)
            instance.satisfaction = validated_data.get('satisfaction', instance.satisfaction)
            instance.doctor = validated_data.get('doctor', instance.doctor)
            instance.save()
            return instance


class UpdateHumanDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanDisease
        fields = ['human', 'disease', 'clinic', 'date_occurred', 'date_treated', 'description', 'satisfaction',
                  'doctor']

        def update(self, instance, validated_data):
            instance.human = validated_data.get('human', instance.human)
            instance.disease = validated_data.get('disease', instance.disease)
            instance.clinic = validated_data.get('clinic', instance.clinic)
            instance.date_occurred = validated_data.get('date_occurred', instance.date_occurred)
            instance.date_treated = validated_data.get('date_treated', instance.date_treated)
            instance.description = validated_data.get('description', instance.description)
            instance.satisfaction = validated_data.get('satisfaction', instance.satisfaction)
            instance.doctor = validated_data.get('doctor', instance.doctor)
            instance.save()
            return instance


class GetAllHumanDiseaseUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseUpdate
        fields = ['id', 'disease_update', 'human_disease']


class CreateHumanDiseaseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseUpdate
        fields = ['disease_update', 'human_disease']

        def save(self, instance, validated_data):
            instance.disease_update = validated_data.get('disease_update', instance.disease_update)
            instance.disease = validated_data.get('disease', instance.disease)
            instance.save()
            return instance


class UpdateHumanDiseaseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseUpdate
        fields = ['disease_update', 'human_disease']

        def update(self, instance, validated_data):
            instance.disease_update = validated_data.get('disease_update', instance.disease_update)
            instance.disease = validated_data.get('disease', instance.disease)
            instance.save()
            return instance


class GetAllHumanMedicalTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanMedicalTests
        fields = ['id', 'human', 'medical_test', 'date_taken', 'clinic', 'satisfaction', 'description', 'file',
                  'results']


class CreateHumanMedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanMedicalTests
        fields = ['human', 'medical_test', 'date_taken', 'clinic', 'ordering_unit', 'satisfaction', 'description',
                  'file', 'results']

        def save(self, instance, validated_data):
            instance.human = validated_data.get('human', instance.human)
            instance.medical_test = validated_data.get('medical_test', instance.medical_test)
            instance.date_taken = validated_data.get('date_taken', instance.date_taken)
            instance.clinic = validated_data.get('clinic', instance.clinic)
            instance.ordering_unit = validated_data.get('ordering_unit', instance.ordering_unit)
            instance.satisfaction = validated_data.get('satisfaction', instance.satisfaction)
            instance.description = validated_data.get('description', instance.description)
            instance.file = validated_data.get('file', instance.file)
            instance.results = validated_data.get('results', instance.results)
            instance.save()
            return instance


class UpdateHumanMedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanMedicalTests
        fields = ['human', 'medical_test', 'date_taken', 'clinic', 'ordering_unit', 'satisfaction', 'description',
                  'file', 'results']

        def update(self, instance, validated_data):
            instance.human = validated_data.get('human', instance.human)
            instance.medical_test = validated_data.get('medical_test', instance.medical_test)
            instance.date_taken = validated_data.get('date_taken', instance.date_taken)
            instance.clinic = validated_data.get('clinic', instance.clinic)
            instance.ordering_unit = validated_data.get('ordering_unit', instance.ordering_unit)
            instance.satisfaction = validated_data.get('satisfaction', instance.satisfaction)
            instance.description = validated_data.get('description', instance.description)
            instance.file = validated_data.get('file', instance.file)
            instance.results = validated_data.get('results', instance.results)
            instance.save()
            return instance


class GetAllHumanWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanWeight
        fields = ['id', 'human', 'date_of_measurement', 'weight']


class CreateHumanWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanWeight
        fields = ['human', 'date_of_measurement', 'weight']

        def save(self, instance, validated_data):
            instance.human = validated_data.get('human', instance.human)
            instance.date_of_measurement = validated_data.get('date_of_measurement', instance.date_of_measurement)
            instance.weight = validated_data.get('weight', instance.weight)
            instance.save()
            return instance


class UpdateHumanWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanWeight
        fields = ['human', 'date_of_measurement', 'weight']

        def update(self, instance, validated_data):
            instance.human = validated_data.get('human', instance.human)
            instance.date_of_measurement = validated_data.get('date_of_measurement', instance.date_of_measurement)
            instance.weight = validated_data.get('weight', instance.weight)
            instance.save()
            return instance


class GetAllHumanGeneralInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanGeneralInformation
        fields = ['id', 'human', 'content']


class CreateHumanGeneralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanGeneralInformation
        fields = ['id', 'human', 'content']

        def save(self, instance, validated_data):
            instance.human = validated_data.get('human', instance.human)
            instance.content = validated_data.get('content', instance.content)
            instance.save()
            return instance


class UpdateHumanGeneralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanGeneralInformation
        fields = ['id', 'human', 'content']

        def update(self, instance, validated_data):
            instance.human = validated_data.get('human', instance.human)
            instance.content = validated_data.get('content', instance.content)
            instance.save()
            return instance
