from django.shortcuts import render,HttpResponse
from .models import Employees
from .form import EmployeeForm,CourseForm,PropertyForm,loginForm,MoivesForm
 
# Create your views here.
def employeeslist(request):
    employees = Employees.objects.all().values()
    print(employees)
    return render(request,"employee/employeelist.html",{"employee":employees})


def employeeFliter(request):
    employee = Employees.objects.filter(name ="Chaitanya Rathod").values()
    print("query 1", employee)

    employee2 = Employees.objects.filter(post = "fferfe").values()
    print("query 2", employee2)

    employee3 = Employees.objects.filter(name = "bhavika",age = 30).values()
    print("query 3", employee3)

    employee4 = Employees.objects.filter(age__gt = 30).values()
    print("query 4", employee4)

    employee5 = Employees.objects.filter(age__gte = 30).values()
    print("query 5", employee5)

    employee6 = Employees.objects.filter(age__lt = 30).values()
    print("query 6", employee6)

    employee7 = Employees.objects.filter(age__lte = 30).values()
    print("query 7", employee7)

    employee8 = Employees.objects.filter(name__exact="Chaitanya Rathod").values()
    print("query 8", employee8)

    employee9 = Employees.objects.filter(name__iexact="chaitanya Rathod").values()
    print("query 9", employee8)

    employee10 = Employees.objects.filter(name__contains="C").values()
    print("query 10", employee10)    

    employee11 = Employees.objects.filter(name__icontains="r").values()
    print("query 11", employee11) 

    employee12 = Employees.objects.filter(name__startswith = "k").values()
    print("query 12", employee12) 

    employee13 = Employees.objects.filter(name__endswith = "l").values()
    print("query 13", employee13) 

    employee14 = Employees.objects.filter(name__istartswith = "c").values()
    print("query 14", employee14) 

    employee15 = Employees.objects.filter(name__iendswith = "D").values()
    print("query 15", employee15) 

    employee16 = Employees.objects.filter(name__in=["raj","jay"]).values()    

    #range
    employee17 = Employees.objects.filter(age__range=[24,30]).values()
    print("query ")    

    #order by
    employee18 = Employees.objects.order_by("age").values()     #asc
    employee19 = Employees.objects.order_by("-age").values()    #desc

    employee20 = Employees.objects.order_by("-salary").values()

    print("query 16", employee16)
    print("query 17", employee17)
    print("query 18", employee18)
    print("query 19", employee19)
    print("query 20", employee20)

    return render(request,'employee/employeeFliter.html')   



def createEmployee(request):
    Employees.objects.create(name="ajay",age=23,salary=23000,post="HR",join_date="2022-01-01")
    return HttpResponse(" created Employee ")


def createEmployeewithForms(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save()
        return HttpResponse(" employee created")
    else:    
        form = EmployeeForm()
        return render(request,"employee/createemployee.html",{"form":form})
    

def CourseFormWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = CourseForm(request.POST)
        form.save()
        return HttpResponse("Course entered")
    else:
        form = CourseForm()
        return render(request,"employee/CourseFormWithForm.html",{"form":form})   


def Property_Form(request):
    print(request.method)
    if request.method == "POST":
        form = PropertyForm(request.POST)
        form.save()
        return HttpResponse("porperty entered")
    else:
        form = PropertyForm()
        return render(request,"employee/PropertyForm.html",{"form":form})  


def login(request):
    print(request.method)
    if request.method == "POST":
        form = loginForm(request.POST)
        form.save()
        return HttpResponse("login successfullay")
    
    else:
        form =loginForm()
        return render(request,"employee/loginForm.html",{"form":form}) 


def Moives_Form(request):
    print(request.method)
    if request.method == "POST":
        form = MoivesForm(request.POST)
        form.save()
        return HttpResponse("moives entered")
    else:
        form =  MoivesForm()
        return render(request,"employee/MoivesForm.html",{"form":form})