# Generated by Django 3.2.4 on 2021-06-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='chassis',
            field=models.CharField(help_text='Saisissez le numéro de chassis', max_length=50, verbose_name='numero de chassis'),
        ),
        migrations.AlterField(
            model_name='car',
            name='registration_number',
            field=models.CharField(help_text="Saisissez l'immatriculation de la voiture", max_length=10, unique=True, verbose_name='immatriculation'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='cylinder',
            field=models.FloatField(help_text='Saisissez le nombre de cylindre', verbose_name='cylindre'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='power',
            field=models.FloatField(help_text='Saisissez la puissance de la voiture', verbose_name='puissance de la voiture'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='prime',
            field=models.FloatField(help_text='Saisissez le montant de la prime', verbose_name='prime'),
        ),
        migrations.AlterField(
            model_name='technicalcheckin',
            name='cost_of_checkIn',
            field=models.FloatField(help_text='Saisissez le montant de la visite technique', verbose_name='montant'),
        ),
    ]
