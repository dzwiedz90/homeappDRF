# Generated by Django 4.0.6 on 2022-07-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DewormingRemedy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deworming_remedy_name', models.CharField(max_length=128, verbose_name='Nazwa środka do odrobaczenia')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Opis (opcjonalne)')),
            ],
        ),
        migrations.CreateModel(
            name='RemedyForTicks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remedy_for_ticks_name', models.CharField(max_length=128, verbose_name='Nazwa środka na klesze')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Opis (opcjonalne)')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentAndDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_and_disease_name', models.CharField(max_length=128, verbose_name='Choroba lub zabieg')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Opis (opcjonalne)')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=64, verbose_name='Nazwa szczepionki')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Opis (opcjonalne)')),
            ],
        ),
        migrations.CreateModel(
            name='VetClinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vet_clinic_name', models.CharField(max_length=128, verbose_name='Nazwa kliniki')),
                ('address', models.CharField(max_length=128, verbose_name='Adres')),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True, verbose_name='Numer telefonu (opcjonalne)')),
                ('opening_hours', models.CharField(max_length=15, verbose_name='Godziny otwarcia')),
            ],
        ),
    ]
