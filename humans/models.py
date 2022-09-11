from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

from human_resources.models import Treatment, MedicalTest, Clinic, Disease


class Human(models.Model):
    GENDER_CHOICES = [('ML', 'mężczyzna'), ('FM', 'kobieta')]

    name = models.CharField('Imię i nazwisko', max_length=64)
    gender = models.CharField('Płeć', max_length=2, choices=GENDER_CHOICES, default='ML')
    date_born = models.DateTimeField('Data urodzenia', validators=[MaxValueValidator(limit_value=timezone.now())])
    height = models.IntegerField('Wzrost')
    current_weight = models.FloatField('Waga')
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)
    photo = models.CharField('Zdjęcie (opcjonalne)', max_length=512)

    def __str__(self):
        return self.name


class HumanTreatment(models.Model):
    SATISFACTION_LEVEL = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]

    human = models.ForeignKey(Human, on_delete=models.PROTECT)
    treatment = models.ForeignKey(Treatment, on_delete=models.PROTECT)
    clinic = models.ForeignKey(Clinic, on_delete=models.PROTECT)
    date_occurred = models.DateTimeField('Data rozpoczecia zabiegu',
                                         validators=[MaxValueValidator(limit_value=timezone.now())])
    date_treated = models.DateTimeField('Data zakończenia leczenia', blank=True, null=True)
    description = models.CharField('Opis zabiegu', max_length=256)
    satisfaction = models.IntegerField('Satysfakcja z leczenia', choices=SATISFACTION_LEVEL, default=5)
    doctor = models.CharField('Lekarz prowadzący (opcjonalne)', max_length=32, blank=True, null=True)
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)

    @property
    def treatment_name(self):
        return self.treatment.treatment_name

    @property
    def clinic_name(self):
        return self.clinic.clinic_name

    def get_class(self):
        return 'HumanTreatment'


class TreatmentUpdate(models.Model):
    treatment_update = models.CharField('Treść', max_length=4096)
    human_treatment = models.ForeignKey(HumanTreatment, on_delete=models.CASCADE)
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)

    @property
    def treatment_update_treatment_id(self):
        return self.human_treatment.id


class HumanDisease(models.Model):
    SATISFACTION_LEVEL = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]

    human = models.ForeignKey(Human, on_delete=models.PROTECT)
    disease = models.ForeignKey(Disease, on_delete=models.PROTECT)
    clinic = models.ForeignKey(Clinic, on_delete=models.PROTECT)
    date_occurred = models.DateTimeField('Data rozpoczecia leczenia',
                                         validators=[MaxValueValidator(limit_value=timezone.now())])
    date_treated = models.DateTimeField('Data zakończenia leczenia', blank=True, null=True)
    description = models.CharField('Opis leczenia', max_length=256)
    satisfaction = models.IntegerField('Satysfakcja z leczenia', choices=SATISFACTION_LEVEL, default=5)
    doctor = models.CharField('Lekarz prowadzący (opcjonalne)', max_length=32, blank=True, null=True)
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)

    @property
    def disease_name(self):
        return self.disease.disease_name

    @property
    def clinic_name(self):
        return self.clinic.clinic_name

    def get_class(self):
        return 'HumanDisease'


class DiseaseUpdate(models.Model):
    disease_update = models.CharField('Treść', max_length=4096)
    human_disease = models.ForeignKey(HumanDisease, on_delete=models.CASCADE)
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)

    @property
    def disease_update_disease_id(self):
        return self.human_disease.id


class HumanMedicalTests(models.Model):
    SATISFACTION_LEVEL = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]

    human = models.ForeignKey(Human, on_delete=models.PROTECT)
    medical_test = models.ForeignKey(MedicalTest, on_delete=models.PROTECT)
    date_taken = models.DateTimeField('Data rozpoczecia leczenia',
                                      validators=[MaxValueValidator(limit_value=timezone.now())])
    clinic = models.ForeignKey(Clinic, on_delete=models.PROTECT, related_name='clinic_performing_test')
    ordering_unit = models.ForeignKey(Clinic, on_delete=models.PROTECT, related_name='ordering_unit')
    satisfaction = models.IntegerField('Satysfakcja z badania', choices=SATISFACTION_LEVEL, default=5)
    description = models.CharField('Opis badania', max_length=256)
    file = models.CharField('Plik (opcjonalne)', max_length=256, blank=True,
                            null=True)
    results = models.CharField('Wyniki (opcjonalne)', max_length=4096, blank=True, null=True)

    @property
    def medical_test_name(self):
        return self.medical_test.medical_test_name

    @property
    def clinic_name(self):
        return self.clinic.clinic_name


class HumanWeight(models.Model):
    human = models.ForeignKey(Human, on_delete=models.PROTECT)
    date_of_measurement = models.DateTimeField('Data pomiaru',
                                               validators=[MaxValueValidator(limit_value=timezone.now())])
    weight = models.FloatField()
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)


class HumanGeneralInformation(models.Model):
    human = models.ForeignKey(Human, on_delete=models.PROTECT)
    content = models.CharField('Opis', max_length=512)
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)

    def get_class(self):
        return 'HumanGeneralInformation'
