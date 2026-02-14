from django.db import models

# Create your models here.
class Services(models.Model):
    ServicesName = models.CharField(max_length=100)
    Description = models.TextField()
    Price = models.IntegerField()
    Duration = models.IntegerField(help_text="Duration in days")
    Is_Activate = models.BooleanField()
    Created_At = models.DateField()

    class Meta:
        db_table = "Services"

    def __str__(self):
        return self.ServicesName    