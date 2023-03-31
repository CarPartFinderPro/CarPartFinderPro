from .user import User
from django.db import models
from .car_part import CarPart


class Favorite(models.Model):
    """
    Model representing a Favorite.
    Fields:
        username (CharField): The user's username.
        part_ad
        create_date (DateTimeField): The date and time the user registered.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Added To favorite by")
    part_ad = models.ForeignKey(CarPart, on_delete=models.CASCADE, verbose_name="Favorite AD")
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
        ordering = ["-create_date"]

    def __str__(self):
        return f"{self.user.username} - {self.part_ad}"
