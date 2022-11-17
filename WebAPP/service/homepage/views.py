from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.template.loader import render_to_string

from .models import Restaurant

def restaurants_catalog(request):
    ctx = {}
    search_data = request.GET.get('search_text')

    if search_data:
        restaurants_response = Restaurant.objects.filter(name__icontains=search_data)
    else:
        restaurants_response = Restaurant.objects.all()

    ctx['restaurants'] = restaurants_response
    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request:
        html = render_to_string(
            template_name='includes/restaurants.html', context={'restaurants': restaurants_response}
        )
        data_dict = {'html_from_view': html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'home/wrapper.html', context=ctx)
