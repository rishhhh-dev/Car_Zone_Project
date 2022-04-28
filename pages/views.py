from django.shortcuts import render
from .models import Team
# Create your views here.

def Home_view(request):
    teams =  Team.objects.all()
    data = {
        'teams':teams,
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