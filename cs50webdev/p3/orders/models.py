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
    # small = false; large = true
    size = models.BooleanField(default=False)
    price = models.IntegerField()

class Subs(models.Model):
    type = models.CharField(max_length=25)
    # small = false; large = True
    size  = models.BooleanField(default=False)
    extra_cheese = models.BooleanField(default=False)
    price = models.IntegerField()

class Toppings(models.Model):
    type = models.CharField(max_length=45)

class Pizzas(models.Model):
    TOPPINGS_CLASS_OPTIONS =  (
        ('Cheese'),
        ('1 topping'),
        ('2 toppings'),
        ('3 toppings'),
        ('Special')
        # restrict number of toppings user can add based on class on Client side
    )
    # regular = False; sicilian = true
    type = models.BooleanField(default=False)
    # small = False; large = true
    size = models.BooleanField(default=False)
    toppings_class = models.CharField(max_length=15, choices=TOPPINGS_CLASS_OPTIONS)
    toppings = models.ManyToManyField('Toppings')
    price = models.IntegerField()
