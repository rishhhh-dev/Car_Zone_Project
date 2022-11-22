from django.shortcuts import render
from .models import Team
from cars.models import car_model
# Create your views here.

def Home_view(request):
    teams =  Team.objects.all()
    featured_cars = car_model.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = car_model.objects.order_by('-created_date')
    # search_fields = car_model.objects.values('model','city','year','body_style')

    model_search = car_model.objects.values_list('model',flat=True).distinct()
    city_search = car_model.objects.values_list('city',flat=True).distinct()
    year_search = car_model.objects.values_list('year',flat=True).distinct()
    body_style_search = car_model.objects.values_list('body_style',flat=True).distinct()

    data = {
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        # 'search_fields':search_fields,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,
    }
    return render(request,'templates/pages/home.html',data)


def About_view(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'templates/pages/about.html',data)

def Contact_view(request):
    return render(request, 'templates/pages/contact.html')

def Service_view(request):
    return render(request, 'templates/pages/service.html')