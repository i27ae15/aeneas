from django.db import models
from .section import Section


class Objective(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
