# Generated by Django 4.0.6 on 2022-09-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(max_length=128, verbose_name='Nazwa placówki')),
                ('address', models.CharField(max_length=128, verbose_name='Adres')),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True, verbose_name='Numer telefonu (opcjonalne)')),
                ('opening_hours', models.CharField(max_length=15, verbose_name='Godziny otwarcia')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=128, verbose_name='Nazwa choroby')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Opis (opcjonalne)')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_test_name', models.CharField(max_length=128, verbose_name='Nazwa badania')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Opis (opcjonalne)')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_name', models.CharField(max_length=128, verbose_name='Nazwa zabiegu')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Opis (opcjonalne)')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
            ],
        ),
    ]
