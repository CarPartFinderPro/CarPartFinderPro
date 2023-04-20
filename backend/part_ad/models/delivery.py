"""
Module containing the Delivery model class.
"""
from django.db import models
from .user import User
from .address import Address


class Delivery(models.Model):
    """
    Model representing a user's delivery address.

    Fields:
        user (ForeignKey): The user to which the delivery address belongs.
        address (ForeignKey): The delivery address.
        address_type (CharField): The type of the address (e.g., 'home', 'work', etc.).
        primary (BooleanField): Whether this address is the primary address for the user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_addresses')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='user_addresses')
    address_type = models.CharField(max_length=50)
    primary = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'address_type')

    def __str__(self):
        return f"{self.user}\'s {self.address_type} address"
