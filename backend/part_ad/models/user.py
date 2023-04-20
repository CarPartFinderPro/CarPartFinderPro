"""
Module containing the User model class.
"""
from django.db import models


class User(models.Model):
    """
    Model representing a user.

    Fields:
        username (CharField): The user's username.
        password (CharField): The user's password.
        active (BooleanField): Flag indicating if the user is active.
        email (EmailField): The user's email address.
        mobile (CharField): The user's mobile phone number - contains area code.
        registration_date (DateTimeField): The date and time the user registered.
    """
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=40, default='')
    registration_date = models.DateTimeField()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username} ({self.email})"

    def set_inactive(self):
        """
        Sets the user as inactive.
        """
        self.active = False
        self.save()

    def set_active(self):
        """
        Sets the user as active.
        """
        self.active = True
        self.save()
