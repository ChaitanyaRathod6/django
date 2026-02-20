from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        #password1  =--> UserCreationForm.. already exist
        fields = ['username','email','first_name','last_name','role','password1','password2']