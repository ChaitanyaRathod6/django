from . import views
from django.urls import path

urlpatterns = [
    path("employeelist/",views.employeeslist),
    path("employeeFliter/",views.employeeFliter),
    path("createemployee/",views.createEmployee),
    path("createemployeewithForm/",views.createEmployeewithForms),
    path("CourseFormWithForm/",views.CourseFormWithForm),
    path("PropertyForm/",views.Property_Form),
    path("loginForm/",views.login),
    path("MoivesForm/",views.Moives_Form),
]