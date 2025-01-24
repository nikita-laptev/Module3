from django.db import models

class Mission(models.Model):
    """
    Модель для миссий.
    """
    name = models.CharField(max_length=100)
    launch_date = models.DateTimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Landing(models.Model):
    """
    Модель для приземлений.
    """
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    landing_date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'Приземление {self.mission.name} в {self.landing_date}'
