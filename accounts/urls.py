from django.urls import path
from .views import *


urlpatterns = [
    path('register/',Register,name='register'),
    path('login/',Login,name='login'),
    path('dashboard/',Dashboard,name='dashboard'),
    path('logout/',Logout,name='logout'),
]