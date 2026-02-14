from django.shortcuts import render,HttpResponse
from .models import Services
from .forms import ServicesForm
# Create your views here.
def services(request):
    if request.method =="POST":
        form = ServicesForm(request.POST)
        form.save()
        return HttpResponse("service entered")
    else:
        form = ServicesForm()
        return render(request,"services/services.html",{"form":form})
    

def ServicesTable(request):
    services = Services.objects.all().values()
    return render(request,"services/servicestable.html",{"services":services})