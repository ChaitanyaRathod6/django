from django.db import models

# Create your models here.
class Employees(models.Model):
    name  = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField()
    post = models.CharField()

    class Meta:
        db_table = "Employees"

    def __str__(self):
        return self.name   


class Course(models.Model):
        name = models.CharField(max_length=100)
        fees = models.IntegerField()
        durations = models.IntegerField()


        class Meta:
              db_table = "Course"


        def __str__(self):
              return self.name   


class Property(models.Model):
    Place = models.CharField(max_length=100)
    Bedroom = models.IntegerField()
    pool = models.BooleanField() 


    class Meta:
          db_table = "Property"

    def __str__(self):
        return self.Place
    


class login(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = "login" 

    def __str__(self):
         return self.name       
    



class Moives(models.Model):
    MoivesName = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    class Meta:
         db_table = "Moives"

    def __str__(self):
        return self.MoivesName     



     
                   