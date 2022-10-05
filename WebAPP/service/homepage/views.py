from django.shortcuts import render

from .models import Restaurant

def restaurants_catalog(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home/homepage.html', {'restaurants': restaurants})
