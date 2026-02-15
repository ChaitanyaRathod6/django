from django.shortcuts import render,HttpResponse,redirect
from .models import Services
from .forms import ServicesForm
# Create your views here.
def services(request):
    if request.method =="POST":
        form = ServicesForm(request.POST)
        form.save()
        return redirect("ServicesTable")
    else:
        form = ServicesForm()
        return render(request,"services/services.html",{"form":form})
    

def ServicesTable(request):
    services = Services.objects.all().values()
    return render(request,"services/servicestable.html",{"services":services})

def ServiceFilter(request):
    services = Services.objects.filter(Price__gt = 2500)
    return render(request,"services/servicefilter.html",{"services":services})


def ServiceDelete(request,id):
    Services.objects.filter(id=id).delete()
    return redirect("ServicesTable")

def ServiceUpdate(request,id):
     #database existing user... id -->
    services = Services.objects.get(id=id) #select * from employee where id = 1
    
    if request.method == "POST":
        form = ServicesForm(request.POST,instance=services)
        form.save()
        return redirect("ServicesTable")
    else:
        form = ServicesForm(instance=services)    
        return render(request,"services/servicesupdate.html",{"form":form})


def SortService(request,id):
    if id == 1:
        services = Services.objects.order_by("id")
    elif id == 2:    
        services = Services.objects.order_by("-id")
    else:
        services = Services.objects.all()    

    return render(request,"services/servicestable.html",{"services":services})    