from django.db import models
from .objetives import Objective

# Create your models here.


class Task(models.Model):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
