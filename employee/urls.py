from . import views
from django.urls import path

urlpatterns = [
    path("employeelist/",views.employeeslist),
    path("employeeFliter/",views.employeeFliter),
]