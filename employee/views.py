from django.shortcuts import render
from .models import Employees
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