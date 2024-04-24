from django.db import models
from .objetives import Objective

# Create your models here.


class Task(models.Model):
    objective: Objective = models.ForeignKey(
        Objective, on_delete=models.CASCADE
        )
    name: str = models.CharField(max_length=100)
    description: str = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.objective}'
