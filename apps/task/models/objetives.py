from django.db import models
from .section import Section

# Create your models here.


class Objectives(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
