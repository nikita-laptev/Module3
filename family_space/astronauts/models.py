from django.db import models

class Astronaut(models.Model):
    """
    Модель космонафта.
    """
    name = models.CharField(max_length=250)
    birthdate = models.DateField(verbose_name='Birthdate')
    rank = models.CharField(max_length=100)
    biography = models.TextField()
    missions = models.ManyToManyField('missions.Mission', related_name='astronauts')

    def __str__(self):
        return f'Космонавт {self.user.username}'
