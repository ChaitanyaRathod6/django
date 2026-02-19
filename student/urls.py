from . import views
from django.urls import path

urlpatterns = [
    path("home/",views.studenthome),
    path("dashboard/",views.dashboard),
    path("details/",views.details),
    path("profile/",views.profile),
    path("marks/",views.marks),
    path("attendance/",views.attendance),
    path("serviceslist/",views.serviceslist,name="serviceList"),
    path("createService/",views.createService,name="createService"),
    path("delete_service/<int:id>",views.delete_service,name='delete_service')
]


