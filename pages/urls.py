from django.urls import path
from .views import *



urlpatterns = [
    path('',Home_view,name='home'),
    path('about/',About_view,name='about'),
    path('contact/',Contact_view,name='contact'),
    path('service/',Service_view,name='service'),
]
