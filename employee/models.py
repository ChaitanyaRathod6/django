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