from . import views
from django.urls import path

urlpatterns = [
    path("employeelist/",views.employeeslist,name = "employeelist"),
    path("employeeFliter/",views.employeeFliter,name = "employeefilter"),
    path("createemployee/",views.createEmployee),
    path("createemployeewithForm/",views.createEmployeewithForms,name = "createEmployeewithForms"),
    path("CourseFormWithForm/",views.CourseFormWithForm),
    path("PropertyForm/",views.Property_Form),
    path("loginForm/",views.login),
    path("MoivesForm/",views.Moives_Form),
    path("DeleteEmployee/<int:id>",views.DeleteEmployee,name="DeleteEmployee"),
    path("FilterEmployee/",views.FilterEmployee,name="FilterEmployee"),
    path("SortEmployee/<int:id>",views.SortEmployee,name="SortEmployee"),
    path("UpdateEmployee/<int:id>",views.UpdateEmployee,name="UpdateEmployee")
]