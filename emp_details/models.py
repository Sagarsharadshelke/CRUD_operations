from django.db import models

# Create your models here.
class emp(models.Model):
    emp_name = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    salary = models.IntegerField()
    DOB = models.DateField()
    location = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.emp_name