from .user import User
from django.db import models
from .car_part import CarPart


class Favorite(models.Model):
    """
    Model representing a Favorite.
    Fields:
        user (ForeignKey): The user who added the part to favorites.
        part_ad (ForeignKey): The CarPart object that was added to favorites.
        create_date (DateTimeField): The date and time the part was added to favorites.
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
