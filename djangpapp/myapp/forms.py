from django import forms  
from myapp.models import Student  
from myapp.models import Employees 

class StuForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  

class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)  
    

 
  
class EmployeesForm(forms.ModelForm):  
    class Meta:  
        model = Employees  
        fields = "__all__"  

class StudentsForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input