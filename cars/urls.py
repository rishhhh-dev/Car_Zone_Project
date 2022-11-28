from django.urls import path
from .views import *


urlpatterns = [
    path('cars/',Car_view,name='car'),
    path('<int:id>',Car_detail_view,name='car_detail'),
    path('search/',Car_search,name='search'),
]