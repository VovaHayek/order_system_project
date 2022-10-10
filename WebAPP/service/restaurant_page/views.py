from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView

from homepage.models import Restaurant, Food, Order

class RestaurantDetailView(DetailView):
    model = Restaurant

    def get_context_data(self, **kwargs):
        index = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['restaurant_food'] = Food.objects.filter(restaurant=index)
        return context

    def post(self, request, **kwargs):
        index = self.kwargs['pk']
        if request.method == "POST":
            order_restaurant = request.POST.get('restaurant')
            order_dishes = request.POST.getlist('food[]')
            order_amount = request.POST.get('amount')
            if order_restaurant and order_dishes and order_amount:
                order = Order.objects.create(restaurant_id=order_restaurant)
                order.dishes.set([eval(i) for i in order_dishes])
                order.amount = order_amount
                order.save()
        return redirect('/restaurant/' + str(index))

