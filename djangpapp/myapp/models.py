from django.db import models

# Create your models here.
class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  


class Student(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    contact    = models.IntegerField()  
    email      = models.EmailField(max_length=50)  
    age        = models.IntegerField()  
    class Meta:  
        db_table = "student"




class Employees(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employees"  