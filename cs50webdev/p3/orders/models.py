from django.db import models
from datetime import datetime

# Create your models here.
class Orders(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=14)
    date = models.DateTimeField(default=datetime.now, blank=True)
    pizza = models.ForeignKey(Pizza, )

    def __str__(self):
        return f'Ordered @ {self.date}, Customer: {self.name}, Phone: {self.phone}\n {self.pizza}'


class Pizza(models.Model):
    STYLE = (
        'sicilian',
        'regular'
    )
    type = models.CharField(choices=STYLE)

    PIZZA_SIZE = (
        'small',
        'large'
    )
    size = models.CharField(choices=PIZZA_SIZE)

    toppings = models.ManyToManyField(Toppings)


class Toppings(models.Model):
    TOPPINGS = (
        'pepperoni',
        'sausage',
        'mushrooms',
        'onions',
        'ham',
        'canadian_bacon',
        'pineapple',
        'eggplant',
        'tomato&basil',
        'green_peppers',
        'hamburger',
        'spinach',
        'artichoke',
        'buffalo_chicken',
        'anchovies',
        'black_olives',
        'fresh_garlic',
        'zuchinni'
    )
    topping = models.CharField(choices=TOPPINGS)

    regular =
        ('small', (
            ('cheese', 12.20),
            ('1', 13.30),
            ('2', 14.70),
            ('3', 15.70),
            ('special', 17.25)
        )),
        ('large', (
            ('cheese', 17.45),
            ('1', 19.45),
            ('2', 21.45),
            ('3', 23.45),
            ('special', 25.45)
        ))
    sicilian =
        ('small', (
            ('cheese', 23.45),
            ('1', 25.45),
            ('2', 27.45),
            ('3', 28.45),
            ('special', 29.45)
        )),
        ('large', (
            ('cheese', 37.70),
            ('1', 39.70),
            ('2', 41.70),
            ('3', 43.70),
            ('special', 44.70)
        ))
