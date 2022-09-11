# Generated by Django 4.0.6 on 2022-09-11 08:25

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('human_resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Imię i nazwisko')),
                ('gender', models.CharField(choices=[('ML', 'mężczyzna'), ('FM', 'kobieta')], default='ML', max_length=2, verbose_name='Płeć')),
                ('date_born', models.DateTimeField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.datetime(2022, 9, 11, 8, 25, 49, 771315, tzinfo=utc))], verbose_name='Data urodzenia')),
                ('height', models.IntegerField(verbose_name='Wzrost')),
                ('current_weight', models.FloatField(verbose_name='Waga')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
                ('photo', models.CharField(max_length=512, verbose_name='Zdjęcie (opcjonalne)')),
            ],
        ),
        migrations.CreateModel(
            name='HumanTreatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_occurred', models.DateTimeField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.datetime(2022, 9, 11, 8, 25, 49, 771653, tzinfo=utc))], verbose_name='Data rozpoczecia zabiegu')),
                ('date_treated', models.DateTimeField(blank=True, null=True, verbose_name='Data zakończenia leczenia')),
                ('description', models.CharField(max_length=256, verbose_name='Opis zabiegu')),
                ('satisfaction', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=5, verbose_name='Satysfakcja z leczenia')),
                ('doctor', models.CharField(blank=True, max_length=32, null=True, verbose_name='Lekarz prowadzący (opcjonalne)')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='human_resources.clinic')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='humans.human')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='human_resources.treatment')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_update', models.CharField(max_length=4096, verbose_name='Treść')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
                ('human_treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='humans.humantreatment')),
            ],
        ),
        migrations.CreateModel(
            name='HumanWeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_measurement', models.DateTimeField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.datetime(2022, 9, 11, 8, 25, 49, 774222, tzinfo=utc))], verbose_name='Data pomiaru')),
                ('weight', models.FloatField()),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='humans.human')),
            ],
        ),
        migrations.CreateModel(
            name='HumanMedicalTests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_taken', models.DateTimeField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.datetime(2022, 9, 11, 8, 25, 49, 773684, tzinfo=utc))], verbose_name='Data rozpoczecia leczenia')),
                ('satisfaction', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=5, verbose_name='Satysfakcja z badania')),
                ('description', models.CharField(max_length=256, verbose_name='Opis badania')),
                ('file', models.CharField(blank=True, max_length=256, null=True, verbose_name='Plik (opcjonalne)')),
                ('results', models.CharField(blank=True, max_length=4096, null=True, verbose_name='Wyniki (opcjonalne)')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clinic_performing_test', to='human_resources.clinic')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='humans.human')),
                ('medical_test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='human_resources.medicaltest')),
                ('ordering_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ordering_unit', to='human_resources.clinic')),
            ],
        ),
        migrations.CreateModel(
            name='HumanGeneralInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=512, verbose_name='Opis')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='humans.human')),
            ],
        ),
        migrations.CreateModel(
            name='HumanDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_occurred', models.DateTimeField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.datetime(2022, 9, 11, 8, 25, 49, 772942, tzinfo=utc))], verbose_name='Data rozpoczecia leczenia')),
                ('date_treated', models.DateTimeField(blank=True, null=True, verbose_name='Data zakończenia leczenia')),
                ('description', models.CharField(max_length=256, verbose_name='Opis leczenia')),
                ('satisfaction', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=5, verbose_name='Satysfakcja z leczenia')),
                ('doctor', models.CharField(blank=True, max_length=32, null=True, verbose_name='Lekarz prowadzący (opcjonalne)')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='human_resources.clinic')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='human_resources.disease')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='humans.human')),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_update', models.CharField(max_length=4096, verbose_name='Treść')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Zarchiwizowany?')),
                ('human_disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='humans.humandisease')),
            ],
        ),
    ]