from django.shortcuts import render
from django.views.generic.detail import DetailView

from homepage.models import Restaurant, Food, Order

class RestaurantDetailView(DetailView):
    model = Restaurant

    def get_context_data(self, **kwargs):
        index = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['restaurant_food'] = Food.objects.filter(restaurant=index)
        return context