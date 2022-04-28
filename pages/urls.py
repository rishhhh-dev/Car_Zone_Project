from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',Home_view,name='home'),
    path('about/',About_view,name='about'),
    path('contact/',Contact_view,name='contact'),
    path('service/',Service_view,name='service'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
