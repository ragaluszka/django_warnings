from django.db import models
from django.utils.timezone import now

# Create your models here.

class Warning(models.Model):
    Voltage = [
        (1, '6kV'),
        (2, '15kv'),
        (3, '30kv'),
        (4, '110kV'),
        (5, 'Puste'),
    ]
    name = models.CharField(max_length=255, blank=False, unique=True)
    voltage = models.CharField(choices=Voltage, max_length=5, default=5)
    opis = models.TextField(max_length=1024,  default='PUSTY')
    date_add = models.DateTimeField(auto_now_add=True)
    date_now = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

