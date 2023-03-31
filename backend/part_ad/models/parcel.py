from django.db import models
from .user import User
from .delivery import Delivery


class Parcel(models.Model):
    """
    Model representing a parcel.
    Fields:
        sender (ForeignKey): The user sending the package.
        recipient (ForeignKey): The user receiving the package.
        weight (FloatField): The weight of the package.
        tracking_number (CharField): The package's tracking number.
        status (CharField): The current status of the package (e.g., 'delivered', 'in transit', etc.).
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    weight = models.FloatField()
    tracking_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Package {self.tracking_number} from {self.sender.username} to {self.recipient.username}"
