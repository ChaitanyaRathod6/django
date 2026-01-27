from django.http import HttpResponse  
from django.shortcuts import render  
def aboutus(request):
    return HttpResponse("aboutus")


def contactus(request):
    return render(request, "contactus.html")


def homepage(request):
    return render(request,"homepage.html")

def movies(request):
    return render(request,"movies.html")

def shows(request):
    return render(request,"shows.html")

def news(request):
    return render(request,"news.html")