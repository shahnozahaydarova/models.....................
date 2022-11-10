from django.db import models


class Odam(models.Model):
    ism = models.CharField(max_length=15)
    familiya = models.CharField(max_length=18)
    yosh = models.IntegerField(default=16)

class Gul(models.Model):
    tur = models.CharField(max_length=14)
    rang = models.CharField(max_length=8)
    