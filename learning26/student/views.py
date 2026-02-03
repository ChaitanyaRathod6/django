from django.shortcuts import render

# Create your views here.
def studenthome(request):
    return render(request,"student/home.html")

def dashboard(request):
    return render(request, "student/dashboard.html")


def details(request):
    student = {
        "name":"Chaitanya",
        "age":22,
        "course":"Django",
        "city":"Hyderabad"
    }
    return render(request,"student/details.html",student)

def profile(request):
    data = {
        "school":"ABC High School",
        "grade":"12th",
        "section":"A",
        "roll_number":23
    }
    return render(request,"student/profile.html",data)

def marks(request):
    marks = {
        "name": "Chaitanya",
        "maths":95,
        "science":88,
        "english":92,
        "history":85
    }
    return render(request,"student/marks.html",marks)



def attendance(request):
    attendance = {
        "name": "Chaitanya",
        "total_classes": 180,
        "classes_attended": 170,
        "attendance_percentage": 94.4
    }
    return render(request,"student/attendance.html",attendance)