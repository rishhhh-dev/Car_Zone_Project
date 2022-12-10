from django.urls import path
from .views import *


urlpatterns = [
   path('enquiry/',Enquiry,name='enquiry'),
]