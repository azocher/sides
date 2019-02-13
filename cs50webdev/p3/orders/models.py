from django.db import models
from datetime import datetime

# Create your models here.
class Pasta(models.Model):
    PASTAS = (
        ('Baked Ziti w/ Mozzarella', 6.5),
        ('Baked Ziti w/ Meatballs', 8.75),
        ('Baked Ziti w/ Chicken', 9.75)
    )

    type = models.CharField()
