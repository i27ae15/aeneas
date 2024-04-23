from django.db import models
from .objetives import Objectives

# Create your models here.


class Task(models.Model):
    objectives = models.ForeignKey(Objectives, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
