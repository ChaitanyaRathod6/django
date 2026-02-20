from . import views
from django.urls import path

urlpatterns = [
    path("register/",views.registerUser,name="register")
]