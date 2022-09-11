from django.forms import ModelForm

from humans.models import Human, HumanTreatment, HumanDisease, HumanMedicalTests, HumanWeight, HumanGeneralInformation, \
    TreatmentUpdate, DiseaseUpdate
from human_resources.models import Treatment, Disease, MedicalTest, Clinic


class HumanForm(ModelForm):
    class Meta:
        model = Human
        fields = ['name', 'gender', 'date_born', 'height', 'current_weight', 'is_archived', 'photo']


class HumanTreatmentForm(ModelForm):
    class Meta:
        model = HumanTreatment
        fields = ['human', 'treatment', 'clinic', 'date_occurred', 'date_treated', 'description', 'satisfaction',
                  'doctor', 'is_archived']


class CreateHumanTreatmentForm(ModelForm):
    class Meta:
        model = HumanTreatment
        fields = ['human', 'treatment', 'clinic']


class HumanDiseaseForm(ModelForm):
    class Meta:
        model = HumanDisease
        fields = ['human', 'disease', 'clinic', 'date_occurred', 'date_treated', 'description', 'satisfaction',
                  'doctor', 'is_archived']


class CreateHumanDiseaseForm(ModelForm):
    class Meta:
        model = HumanDisease
        fields = ['human', 'disease', 'clinic']


class HumanMedicalTestForm(ModelForm):
    class Meta:
        model = HumanMedicalTests
        fields = ['human', 'medical_test', 'date_taken', 'clinic', 'ordering_unit', 'satisfaction', 'description',
                  'file', 'results']


class CreateHumanMedicalTestForm(ModelForm):
    class Meta:
        model = HumanMedicalTests
        fields = ['human', 'medical_test', 'date_taken', 'clinic', 'ordering_unit', 'satisfaction', 'description',
                  'file', 'results']


class HumanWeightForm(ModelForm):
    class Meta:
        model = HumanWeight
        fields = ['human', 'date_of_measurement', 'weight', 'is_archived']


class HumanInformationtForm(ModelForm):
    class Meta:
        model = HumanGeneralInformation
        fields = ['human', 'content', 'is_archived']


class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = ['treatment_name', 'description', 'is_archived']


class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = ['disease_name', 'description', 'is_archived']


class TestForm(ModelForm):
    class Meta:
        model = MedicalTest
        fields = ['medical_test_name', 'description', 'is_archived']


class ClinicForm(ModelForm):
    class Meta:
        model = Clinic
        fields = ['clinic_name', 'address', 'phone_number', 'opening_hours', 'is_archived']


class TreatmentUpdateForm(ModelForm):
    class Meta:
        model = TreatmentUpdate
        fields = ['treatment_update', 'human_treatment', 'is_archived']


class DiseaseUpdateForm(ModelForm):
    class Meta:
        model = DiseaseUpdate
        fields = ['disease_update', 'human_disease', 'is_archived']
