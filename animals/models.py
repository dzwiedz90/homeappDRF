from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

from animal_resources.models import DewormingRemedy, TreatmentAndDisease, VetClinic, RemedyForTicks, Vaccine


class Animal(models.Model):
    GENDER_CHOICES = [('ML', 'samiec'), ('FM', 'samica')]

    animal_name = models.CharField('Imię', max_length=64)
    species = models.CharField('Gatunek', max_length=64)
    breed = models.CharField('Rasa', max_length=128)
    gender = models.CharField('Płeć', max_length=2, choices=GENDER_CHOICES, default='ML')
    date_born = models.DateTimeField('Data urodzenia', validators=[MaxValueValidator(limit_value=timezone.now())])
    date_died = models.DateTimeField('Data śmierci (opcjonalne)', blank=True, null=True)
    current_weight = models.FloatField('Waga')
    fur_ointment = models.CharField('Maść', max_length=32)
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)
    photo = models.ImageField('Zdjęcie (opcjonalne)', upload_to='animal_resources/animal_photos', blank=True,
                              null=True)

    def __str__(self):
        return self.animal_name


class AnimalDeworming(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    deworming_date = models.DateTimeField('Data odrobaczenia',
                                          validators=[MaxValueValidator(limit_value=timezone.now())])
    deworming_expiration_date = models.DateTimeField('Data ważności')
    deworming_remedy = models.ForeignKey(DewormingRemedy, on_delete=models.PROTECT)

    @property
    def deworming_remedy_name(self):
        return self.deworming_remedy.deworming_remedy_name

    @property
    def animal_name(self):
        return self.animal.animal_name


class AnimalTreatmentAndDisease(models.Model):
    SATISFACTION_LEVEL = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]

    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    treatment_and_disease = models.ForeignKey(TreatmentAndDisease, on_delete=models.PROTECT)
    vet_clinic = models.ForeignKey(VetClinic, on_delete=models.PROTECT)
    date_occurred = models.DateTimeField('Data rozpoczecia leczenia',
                                         validators=[MaxValueValidator(limit_value=timezone.now())])
    date_treated = models.DateTimeField('Data zakończenia leczenia')
    meds_given = models.CharField('Podane leki (opcjonalne)', max_length=256, blank=True, null=True)
    treatment_cost = models.IntegerField('Koszt leczenia')
    description = models.CharField('Opis leczenia', max_length=256)
    satisfaction = models.IntegerField('Satysfakcja z leczenia', choices=SATISFACTION_LEVEL, default=5)
    doctor = models.CharField('Lekarz prowadzący (opcjonalne)', max_length=32, blank=True, null=True)

    @property
    def treatment_and_disease_name(self):
        return self.treatment_and_disease.treatment_and_disease_name

    @property
    def vet_clinic_name(self):
        return self.vet_clinic.vet_clinic_name

    @property
    def animal_name(self):
        return self.animal.animal_name


class AnimalRemedyForTicks(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    remedy_for_ticks = models.ForeignKey(RemedyForTicks, on_delete=models.PROTECT)
    application_date = models.DateTimeField('Data aplikacji',
                                            validators=[MaxValueValidator(limit_value=timezone.now())])
    expiration_date = models.DateTimeField('Data ważności')

    @property
    def remedy_for_ticks_name(self):
        return self.remedy_for_ticks.remedy_for_ticks_name

    @property
    def animal_name(self):
        return self.animal.animal_name


class AnimalVaccine(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.PROTECT)
    date_of_vaccination = models.DateTimeField('Data szczepienia',
                                               validators=[MaxValueValidator(limit_value=timezone.now())])
    date_of_expiration = models.DateTimeField('Data ważności')

    @property
    def animal_name(self):
        return self.animal.animal_name

    @property
    def vaccine_name(self):
        return self.vaccine.vaccine_name


class AnimalWeight(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    date_of_measurement = models.DateTimeField('Data pomiaru',
                                               validators=[MaxValueValidator(limit_value=timezone.now())])
    weight = models.FloatField()

    @property
    def animal_name(self):
        return self.animal.animal_name


class AnimalGeneralInformation(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    content = models.CharField('Opis', max_length=512)

    @property
    def animal_name(self):
        return self.animal.animal_name
