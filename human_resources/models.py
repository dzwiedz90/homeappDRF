from django.db import models


class Treatment(models.Model):
    treatment_name = models.CharField('Nazwa zabiegu', max_length=128)
    description = models.CharField('Opis (opcjonalne)', max_length=256, blank=True, null=True)
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)

    def __str__(self):
        return self.treatment_name


class Disease(models.Model):
    disease_name = models.CharField('Nazwa choroby', max_length=128)
    description = models.CharField('Opis (opcjonalne)', max_length=256, blank=True, null=True)
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)

    def __str__(self):
        return self.disease_name


class MedicalTest(models.Model):
    medical_test_name = models.CharField('Nazwa badania', max_length=128)
    description = models.CharField('Opis (opcjonalne)', max_length=256, blank=True, null=True)
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)

    def __str__(self):
        return self.medical_test_name


class Clinic(models.Model):
    clinic_name = models.CharField('Nazwa placówki', max_length=128)
    address = models.CharField('Adres', max_length=128)
    phone_number = models.CharField('Numer telefonu (opcjonalne)', max_length=16, blank=True, null=True)
    opening_hours = models.CharField('Godziny otwarcia', max_length=15)
    is_archived = models.BooleanField('Zarchiwizowany?', default=False)

    def __str__(self):
        return self.clinic_name
