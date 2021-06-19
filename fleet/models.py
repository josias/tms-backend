from django.db import models
from django.utils.translation import gettext_lazy as _
# Cette fonction est utilisée pour formater les URL
from django.urls import reverse

import trip.models
from core.models import TimestampModel


class CarModel(TimestampModel):
    class FuelCategory(models.TextChoices):
        DIESEL = 'DZ', _('Diesel')
        ESSENCE = 'ES', _('Essence')

    # Fields
    name = models.CharField(unique=True,
                            max_length=20,
                            verbose_name="modèle de la voiture",
                            blank=False,
                            help_text="Saisissez le modèle de la voiture")
    firm = models.CharField(max_length=20,
                            verbose_name="marque",
                            blank=False,
                            help_text="Saisissez le modèle de la voiture")
    power = models.FloatField(verbose_name='puissance de la voiture',
                              blank=False,
                              help_text="Saisissez la puissance de la voiture")
    cylinder = models.FloatField(verbose_name='cylindre',
                                 blank=False,
                                 help_text="Saisissez le nombre de cylindre")
    fuel_consumption = models.FloatField(blank=False,
                                         verbose_name="Consommation aux 100Km",
                                         help_text="Saisissez la consommation en litre de carburant")
    fuel_type = models.CharField(verbose_name='type de carburant',
                                 blank=False,
                                 max_length=2,
                                 choices=FuelCategory.choices,
                                 default=FuelCategory.ESSENCE,
                                 help_text="Choisissez le type de carburant")

    class Meta:
        verbose_name = 'modèle de voiture',
        verbose_name_plural = 'modèles de voiture'
        # classement inversé
        ordering = ['-name']

    # Methods
    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.name

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('carmodel-detail', args=[str(self.id)])


class Car(CarModel):
    registration_number = models.CharField(unique=True,
                                           blank=False,
                                           verbose_name='immatriculation',
                                           max_length=10,
                                           help_text="Saisissez l\'immatriculation de la voiture")
    chassis = models.CharField(blank=False,
                               verbose_name='numero de chassis',
                               max_length=50,
                               help_text="Saisissez le numéro de chassis")

    # Methods
    class Meta:
        verbose_name = 'voiture'
        verbose_name_plural = 'flotte'
        ordering = ['registration_number']

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.registration_number

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('car-detail', args=[str(self.id)])

    """#une methode pour déterminer le coût des entretiens et réparations sur une période donnée
    #une methode pour déterminer le coût global impôts, assurance, entretien, carburant sur une année
    #une methode pour déterminer le cout du carburant sur une période en fonction d'un utilisateur"""


class Insurance(TimestampModel):
    insurance_company = models.ForeignKey("trip.Organization",
                                          verbose_name='Assureur',
                                          related_name='Insurance_Company',
                                          on_delete=models.CASCADE)
    vehicle = models.OneToOneField(Car,
                                   verbose_name='véhicule',
                                   on_delete=models.CASCADE)
    policy_number = models.IntegerField(verbose_name='police d\'assurance')
    activation_date = models.DateField(verbose_name='date d\'activation')
    expiration_date = models.DateField(verbose_name='date d\'expiration')
    prime = models.FloatField(verbose_name='prime',
                              help_text='Saisissez le montant de la prime')

    class Meta:
        verbose_name = 'Assurance'
        verbose_name_plural = 'Assurances'
        ordering = ['-expiration_date']

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.policy_number

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('insurance-detail', args=[str(self.id)])


class Tax(TimestampModel):
    vehicle = models.OneToOneField(Car,
                                   verbose_name='véhicule',
                                   on_delete=models.CASCADE)
    tax_amount = models.FloatField(verbose_name='montant de la tax',
                                   max_length=20)
    date_of_tax_payment = models.DateField(verbose_name='date du paiement de la taxe')
    next_due_date = models.DateField(verbose_name='date du prochain paiement de la taxe')

    class Meta:
        verbose_name = 'Taxe sur véhicule'
        verbose_name_plural = 'Taxes sur véhicule'
        ordering = ['-date_of_tax_payment']

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.tax_amount

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('tax-detail', args=[str(self.id)])


class TechnicalCheckIn(TimestampModel):
    vehicle = models.OneToOneField(Car,
                                   verbose_name='véhicule',
                                   on_delete=models.CASCADE)
    check_in_number = models.CharField(verbose_name='Référence de la visite',
                                       max_length=20)
    comment = models.TextField(verbose_name='commentaire')
    date_of_checkIn = models.DateField(verbose_name='date de la visite')
    date_of_next_checkIn = models.DateField(verbose_name='date de la prochaine visite')
    cost_of_checkIn = models.FloatField(verbose_name='montant',
                                        help_text='Saisissez le montant de la visite technique')

    class Meta:
        verbose_name = 'Visite Technique'
        verbose_name_plural = 'Visites Techniques'
        ordering = ['-date_of_checkIn']

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.check_in_number

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('control-detail', args=[str(self.id)])


class Service(TimestampModel):
    class Category(models.TextChoices):
        REPAIR = 'RE', _('Repair')
        ROUTINE = 'RO', _('Routine')

    vehicle = models.OneToOneField(Car,
                                   verbose_name='véhicule',
                                   on_delete=models.CASCADE)
    service_supplier = models.ForeignKey("trip.Organization",
                                         verbose_name='fournisseur',
                                         related_name='Service_Company',
                                         on_delete=models.CASCADE)
    order_id = models.CharField(max_length=20,
                                verbose_name='bon de commande')
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.ROUTINE,
    )
    date_of_service = models.DateField(verbose_name='date')
    next_date = models.DateField(verbose_name='prochaine date')
    cost_of_service = models.FloatField(verbose_name='coût',
                                        help_text='Saisir le coût')
    cost_of_lubes = models.FloatField(verbose_name='coût des lubrifiants',
                                      help_text='Saisir le coût des lubrifiants',
                                      null=True,
                                      blank=True)
    cost_of_parts = models.FloatField(verbose_name='coût des pièces',
                                      help_text='Saisir le coût des pièces de rechanges',
                                      null=True,
                                      blank=True)

    class Meta:
        verbose_name = 'Maintenance'
        verbose_name_plural = 'Maintenances'
        ordering = ['-next_date']

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.order_id

    def get_absolute_url(self):
        """Cette fonction est n'est requise par Django, Elle est utilse pour détailler le contenu d'un objet."""
        return reverse('maintenance-detail', args=[str(self.id)])
