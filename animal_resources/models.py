from django.db import models


class RemedyForTicks(models.Model):
    remedy_for_ticks_name = models.CharField('Nazwa środka na klesze', max_length=128)
    description = models.CharField('Opis (opcjonalne)', max_length=256, blank=True, null=True)

    def __str__(self):
        return self.remedy_for_ticks_name


class TreatmentAndDisease(models.Model):
    treatment_and_disease_name = models.CharField('Choroba lub zabieg', max_length=128)
    description = models.CharField('Opis (opcjonalne)', max_length=256, blank=True, null=True)

    def __str__(self):
        return self.treatment_and_disease_name


class Vaccine(models.Model):
    vaccine_name = models.CharField('Nazwa szczepionki', max_length=64)
    description = models.CharField('Opis (opcjonalne)', max_length=256, blank=True, null=True)

    def __str__(self):
        return self.vaccine_name


class VetClinic(models.Model):
    vet_clinic_name = models.CharField('Nazwa kliniki', max_length=128)
    address = models.CharField('Adres', max_length=128)
    phone_number = models.CharField('Numer telefonu (opcjonalne)', max_length=16, blank=True, null=True)
    opening_hours = models.CharField('Godziny otwarcia', max_length=15)

    def __str__(self):
        return self.vet_clinic_name


class DewormingRemedy(models.Model):
    deworming_remedy_name = models.CharField('Nazwa środka do odrobaczenia', max_length=128)
    description = models.CharField('Opis (opcjonalne)', max_length=256, blank=True, null=True)

    def __str__(self):
        return self.deworming_remedy_name
