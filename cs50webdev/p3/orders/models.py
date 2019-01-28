from django.db import models
from datetime import datetime

# Create your models here.
class Toppings(models.Model):
    TOPPING_OPTIONS = (
        ('pepperoni', 'pepperoni'),
        ('sausage', 'sausage'),
        ('mushrooms', 'mushrooms'),
        ('onions', 'onions'),
        ('ham', 'ham'),
        ('canadian bacon', 'canadian bacon'),
        ('pineapple', 'pineapple'),
        ('eggplant', 'eggplant'),
        ('tomato & basil', 'tomato & basil'),
        ('green_peppers', 'green_peppers'),
        ('hamburger', 'hamburger'),
        ('spinach', 'spinach'),
        ('artichoke', 'artichoke'),
        ('buffalo chicken', 'buffalo chicken'),
        ('anchovies', 'anchovies'),
        ('black olives', 'black olives'),
        ('fresh garlic', 'fresh garlic'),
        ('zuchinni', 'zuchinni')
    )
    topping = models.CharField(max_length=25, choices=TOPPING_OPTIONS, default=None)

    def __str__(self):
        return f'{self.topping}'

class Item(models.Model):
    type = models.CharField(max_length=100)
    SIZE = (
        ('small', 'small'),
        ('large', 'large'),
        ('none', 'none')
    )
    size = models.CharField(max_length=9, choices=SIZE, default="none")
    toppings = models.ManyToManyField(Toppings, blank=True)
    toppings_class = models.CharField(max_length=9, default="None", blank=True)
    price = models.FloatField(null=True, default=None, blank=True)
    amount = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.size}, {self.type} ordered. Will cost {self.price}.'

class Orders(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=14)
    date = models.DateTimeField(default=datetime.now, blank=True)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f'Ordered @ {self.date}, Customer: {self.name}, Phone: {self.phone}'
