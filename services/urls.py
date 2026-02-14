from . import views 
from django.urls import path

urlpatterns = [
    path("Service/",views.services),
    path("ServicesTable/",views.ServicesTable),
]