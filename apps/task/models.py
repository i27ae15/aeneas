from django.db import models

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Objectives(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Task(models.Model):
    objectives = models.ForeignKey(Objectives, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
