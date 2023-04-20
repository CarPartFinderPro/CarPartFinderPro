"""
Module containing the CarPart model class.
"""
from django.db import models
from .user import User


class CarPart(models.Model):
    """
    Model representing a car part advertisement.

    Fields:
        title (CharField): The title of the car part advertisement.
        description (TextField): A detailed description of the car part.
        brand (CharField): The brand of the car that the part is compatible with.
        model (CharField): The model of the car that the part is compatible with.
        year_from (IntegerField): The starting year of car production the part is compatible with.
        year_to (IntegerField): The ending year of car production the part is compatible with.
        part_number (CharField): The part number, if available (optional).
        price (DecimalField): The price of the car part.
        color (charField): Color's model
        condition (CharField): The condition of the car part (new or used).
        quality (CharField): The quality of the car part (O, OE, P, etc.).
        quantity (DecimalField): The quantity of the car part
        seller (ForeignKey): The seller of the car part (ForeignKey relationship with the User model).
        active_until (DateTimeField): The date the advertisement is active until
        created_at (DateTimeField): The date the advertisement was created.
        updated_at (DateTimeField): The date the advertisement was last updated.
    """
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    brand = models.CharField(max_length=50, verbose_name="Brand")
    model = models.CharField(max_length=50, verbose_name="Model")
    year_from = models.IntegerField(verbose_name="Year from")
    year_to = models.IntegerField(verbose_name="Year to")
    part_number = models.CharField(max_length=100, verbose_name="Part number", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    color_model = models.CharField(max_length=40, verbose_name='Color model')
    condition = models.CharField(max_length=50, choices=[('new', 'New'), ('used', 'Used')], verbose_name="Condition")
    quality = models.CharField(max_length=50,
                               choices=[('O', 'O'), ('OE', 'OE'), ('P', 'P'), ('PJ', 'PJ'), ('Z', 'Z'), ('ZJ', 'ZJ')],
                               verbose_name="Quality")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Seller")
    active_until = models.DateTimeField(auto_now_add=True, verbose_name="Active time")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update date")

    class Meta:
        verbose_name = "Car Part"
        verbose_name_plural = "Car Parts"

    def __str__(self):
        return str(self.title)
