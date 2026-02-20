from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    rolechoices = (
        ("admin","admin"),
        ("student","student"),
        ("facutly","faculty"),
    )
    role = models.CharField(max_length=100,choices=rolechoices,null=True,blank=True)