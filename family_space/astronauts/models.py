from django.db import models

class Astronaut(models.Model):
    """
    Модель космонафта.
    """
    biography = models.TextField()
    missions = models.ManyToManyField('missions.Mission', related_name='astronauts')

    def __str__(self):
        return f'Космонавт {self.user.username}'
