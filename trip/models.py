from django.db import models

import fleet.models

"""Cette fonction reverse est utilisée pour formater les URL"""
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import TimestampModel


class Organization(TimestampModel):
    name = models.CharField(max_length=100,
                            verbose_name='dénomination',
                            unique=True,
                            blank=False,
                            help_text="Saisissez le nom de la société")
    address = models.CharField(max_length=100,
                               verbose_name='adresse',
                               help_text="Saisissez l'adresse de la société")

    class Meta:
        verbose_name = 'Société'
        verbose_name_plural = 'Sociétés'

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.name

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('employee-detail', args=[str(self.name)])


class Employee(TimestampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=20,
                            verbose_name='fonction',
                            help_text="Saisissez la fonction de l\'employé au sein de l\'organisation")
    is_tms_manager = models.BooleanField(default=False,
                                         verbose_name='est gestionnaire de tms',
                                         help_text='Définir le role vis-à-vis de tms')

    class Meta:
        verbose_name = 'Employé'
        verbose_name_plural = 'Employés'
        ordering = ['user']

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.user.__str__()

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('employee-detail', args=[str(self.user_id)])


class Mission(TimestampModel):
    reference = models.CharField(max_length=20,
                                 verbose_name='référence',
                                 help_text='saisir référence de la note')
    driver = models.ForeignKey(Employee,
                               on_delete=models.CASCADE,
                               verbose_name='conducteur')
    vehicle = models.ForeignKey("fleet.Car",
                                related_name='Attributed',
                                on_delete=models.CASCADE,
                                verbose_name='vehicule')
    is_permanent = models.BooleanField(default=False,
                                       verbose_name='Est une affectation permanente')
    start_date = models.DateField(verbose_name='date de début')
    end_date = models.DateField(verbose_name='date_de fin',
                                null=True,
                                blank=True)
    odometer_initial_index = models.IntegerField(verbose_name='Compteur initial')
    odometer_final_index = models.IntegerField(verbose_name='Compteur final',
                                               null=True,
                                               blank=True)

    class Meta:
        verbose_name = 'Mission'
        verbose_name_plural = 'Missions'

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.reference

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('employee-detail', args=[str(self.id)])


class Fuel(TimestampModel):
    quantity = models.FloatField(verbose_name='quantité',
                                 help_text='saisir la quantité de carburant payée')
    cost = models.FloatField(verbose_name='coût',
                             help_text='saisir le coût du carburant payée')
    date = models.DateField(verbose_name='date d\'achat',
                            help_text='Saisir la date de paiement')
    odometer_index = models.IntegerField(verbose_name='Compteur index',
                                         help_text='Saisir la date de paiement')
    mission = models.ForeignKey(Mission,
                                on_delete=models.CASCADE,
                                verbose_name='mission concernée',
                                help_text='Choisir la mission concernée')

    class Meta:
        verbose_name = 'Achat de carburant'
        verbose_name_plural = 'Achats de carburant'
        ordering = ['-date']

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet.
        #retourner un string 40L à 50000Fr pour la mission_id"""
        return "{0} litres à {1} francs pour {2}".format(self.quantity, self.cost, self.mission_reference)

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('fuel-detail', args=[str(self.id)])


class Incident(TimestampModel):
    title = models.CharField(verbose_name='quantité',
                             max_length=100,
                             help_text='saisir la quantité de carburant payée')
    description = models.TextField(verbose_name='quantité',
                                   help_text='saisir la quantité de carburant payée')
    date = models.DateField(verbose_name='vehicule',
                            help_text='Saisir la date de paiement')
    mission = models.ForeignKey(Mission,
                                on_delete=models.CASCADE,
                                verbose_name='mission concernée',
                                help_text='Choisir la mission concernée')

    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'
        ordering = ['-date']

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet.
        #retourner un string 40L à 50000Fr pour la mission_id"""
        return self.title

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('fuel-detail', args=[str(self.id)])
