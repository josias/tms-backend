# Generated by Django 3.2.4 on 2021-06-10 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fleet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(help_text="Saisissez la fonction de l'employé au sein de l'organisation", max_length=20, verbose_name='fonction')),
                ('is_tms_manager', models.BooleanField(default=False, help_text='Définir le role vis-à-vis de tms', verbose_name='est gestionnaire de tms')),
            ],
            options={
                'verbose_name': 'Employé',
                'verbose_name_plural': 'Employés',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Saisissez le nom de la société', max_length=100, unique=True, verbose_name='dénomination')),
                ('address', models.CharField(help_text="Saisissez l'adresse de la société", max_length=100, verbose_name='dénomination')),
            ],
            options={
                'verbose_name': 'Société',
                'verbose_name_plural': 'Sociétés',
            },
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reference', models.CharField(help_text='saisir référence de la note', max_length=20, verbose_name='référence')),
                ('is_permanent', models.BooleanField(default=False, verbose_name='Est une affectation permanente')),
                ('start_date', models.DateField(verbose_name='date de début')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='date_de fin')),
                ('odometer_initial_index', models.IntegerField(verbose_name='Compteur initial')),
                ('odometer_final_index', models.IntegerField(verbose_name='Compteur final')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.employee', verbose_name='conducteur')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Attributed', to='fleet.car', verbose_name='vehicule')),
            ],
            options={
                'verbose_name': 'Mission',
                'verbose_name_plural': 'Missions',
            },
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='saisir la quantité de carburant payée', max_length=100, verbose_name='quantité')),
                ('description', models.TextField(help_text='saisir la quantité de carburant payée', verbose_name='quantité')),
                ('date', models.DateField(help_text='Saisir la date de paiement', verbose_name='vehicule')),
                ('mission', models.ForeignKey(help_text='Choisir la mission concernée', on_delete=django.db.models.deletion.CASCADE, to='trip.mission', verbose_name='mission concernée')),
            ],
            options={
                'verbose_name': 'Incident',
                'verbose_name_plural': 'Incidents',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.FloatField(help_text='saisir la quantité de carburant payée', verbose_name='quantité')),
                ('cost', models.FloatField(help_text='saisir la quantité de carburant payée', verbose_name='quantité')),
                ('date', models.DateField(help_text='Saisir la date de paiement', verbose_name='vehicule')),
                ('odometer_index', models.IntegerField(help_text='Saisir la date de paiement', verbose_name='Compteur index')),
                ('mission', models.ForeignKey(help_text='Choisir la mission concernée', on_delete=django.db.models.deletion.CASCADE, to='trip.mission', verbose_name='mission concernée')),
            ],
            options={
                'verbose_name': 'Achat de carburant',
                'verbose_name_plural': 'Achats de carburant',
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.organization'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
