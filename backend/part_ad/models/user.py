from django.db import models


class User(models.Model):
    """
    Model representing a user.
    Fields:
        username (CharField): The user's username.
        password (CharField): The user's password.
        email (EmailField): The user's email address.
        mobile (CharField): The user's mobile phone number - contains area code
        registration_date (DateTimeField): The date and time the user registered.
    """
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    active = models.BooleanField()
    email = models.EmailField()
    mobile = models.CharField(max_length=40)
    registration_date = models.DateTimeField()
