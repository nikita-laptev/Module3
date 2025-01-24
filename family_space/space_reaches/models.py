from django.db import models

class SpaceFlight(models.Model):
    """
    Модель для управления космическими рейсами.
    """
    flight_number = models.CharField(max_length=20, unique=True)
    destination = models.CharField(max_length=100)
    launch_date = models.DateField()
    seats_available = models.IntegerField()

    def __str__(self):
        return f"{self.flight_number} to {self.destination}"
