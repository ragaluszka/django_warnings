from django.db import models
from django.utils.timezone import now

# Create your models here.


class Voltage(models.Model):
    name = models.CharField(max_length=10, blank=False, unique=True)

    def __str__(self):
        return self.name


class Direction(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)

    def __str__(self):
        return self.name


class Warning(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    opis = models.TextField(max_length=1024,  default='PUSTY')
    date_add = models.DateTimeField(auto_now_add=True)
    date_now = models.DateTimeField(auto_now=True)
    direction = models.ManyToManyField(Direction)
    voltage = models.ManyToManyField(Voltage)

    def __str__(self):
        return self.name




