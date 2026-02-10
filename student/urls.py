from . import views
from django.urls import path

urlpatterns = [
    path("home/",views.studenthome),
    path("dashboard/",views.dashboard),
    path("details/",views.details),
    path("profile/",views.profile),
    path("marks/",views.marks),
    path("attendance/",views.attendance),
]


