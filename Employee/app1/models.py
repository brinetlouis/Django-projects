from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    salary=models.IntegerField()
    designation=models.CharField(max_length=50)
    place=models.CharField(max_length=30)
    image=models.ImageField(upload_to='employee')
    department_name=models.CharField(max_length=50)

