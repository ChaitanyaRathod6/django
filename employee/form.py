from django import forms
from .models import Employees,Course,Property,login,Moives

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__" 


class CourseForm(forms.ModelForm): 
    class Meta:
        model = Course
        fields = "__all__"


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property 
        fields = "__all__"       


class loginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = "__all__"   


class MoivesForm(forms.ModelForm):
    class Meta:
        model = Moives
        fields = "__all__"