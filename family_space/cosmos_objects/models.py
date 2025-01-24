from django.contrib.auth.models import User
from django.db import models

class CosmicObject(models.Model):
    """
    Модель для хранения космических объектов.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ссылка на пользователя из стандартной модели Django

    def __str__(self):
        return self.name
