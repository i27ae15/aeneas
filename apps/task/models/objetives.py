from django.db import models
from .section import Section


class Objective(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name: str = models.CharField(max_length=100)
    description: str = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} - {self.section}'
