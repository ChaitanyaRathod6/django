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

def recipe(request):
    ingredients = ["noodles","sauce","cheese","vegetables"]
    data = {
        'name':'maggie',
        "time": 20,
        'ingredients': ingredients
    }
    return render(request,"recipe.html", data)  


def team(request):
    players = ["rohit sharma","suryakumar yadav","hardik pandya","jason holder","kieron pollard"]
    ipl = {
        "teamname" : "mumbai indians",
        "captain" : "rohit sharma",
        "players" : players,
        "trophies" : 5
    }
    
    return render(request, "team.html", ipl)
