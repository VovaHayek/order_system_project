from django.contrib import admin

from .models import Restaurant, Food, Order

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Order)
