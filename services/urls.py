from . import views 
from django.urls import path

urlpatterns = [
    path("Service/",views.services,name="Service"),
    path("ServicesTable/",views.ServicesTable,name="ServicesTable"),
    path("ServiceFilter/",views.ServiceFilter,name="ServiceFilter"),
    path("ServiceDelete/<int:id>",views.ServiceDelete,name="ServiceDelete"),
    path("ServiceUpdate/<int:id>",views.ServiceUpdate,name='ServiceUpdate'),
    path("SortServcies/,<int:id>",views.SortService,name="SortServices")
]