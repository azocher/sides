from django.contrib import admin

from orders.models import Orders, Item, Toppings
# Register your models here.
admin.site.register(Orders)
admin.site.register(Item)
admin.site.register(Toppings)
