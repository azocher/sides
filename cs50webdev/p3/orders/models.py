from django.db import models
from datetime import datetime


# Create your models here.
class Pasta(models.Model):
    type = models.CharField(max_length=25)
    price = models.IntegerField()

class Salad(models.Model):
    type = models.CharField(max_length=25)
    price = models.IntegerField()

class DinnerPlates(models.Model):
    type = models.CharField(max_length=25)
    size = models.BooleanField(default=False)
    price = models.IntegerField()
