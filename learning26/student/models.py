from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField(null=True)


    class Meta:
        db_table  = "student"


class product(models.Model):
    name  = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    stock = models.IntegerField()
    color = models.CharField(null =True, max_length=50) 
    status = models.CharField(default = True)


    class Meta:
        db_table = "product"



class teacher(models.Model):
    Name = models.CharField(max_length= 200)        
    Age = models.IntegerField()
    Subject = models.CharField(max_length=50) 
    salary = models.PositiveBigIntegerField(null = True)
    Email = models.EmailField(null = True) 


    class Meta:
        db_table = "Teacher"     