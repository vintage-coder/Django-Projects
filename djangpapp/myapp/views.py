from django.shortcuts import render,redirect
from myapp.functions.functions import handle_uploaded_file  
import datetime;
# Create your views here.
# Create your views here.  
from django.http import HttpResponse, HttpResponseNotFound 
from django.template import loader  
from myapp.forms import StuForm ,StudentForm ,EmployeesForm,StudentsForm
from django.views.decorators.http import require_http_methods 
from myapp.models import Student  

@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')


def hello(request):  


    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  

 
def index(request):  
    a = 0  
    if a:  
        return HttpResponseNotFound('<h1>Page not found</h1>')  
    else:  
        # now = datetime.datetime.now()  
        # html = "<html><body><h3>Now time is %s.</h3></body></html>" % now 
        template = loader.get_template('index.html') # getting our template
        stu=StuForm()
        student = StudentForm()  

        data=Student.objects.all()
   

        name = {  
        'student':'rahul'  
        }    
        print('the request is',request) 
        # return HttpResponse(template.render(name))
        return render(request,"index.html",{'student':'rahul','form':stu,'form1':student,'student_number':data,})  
        
        
     # rendering the template in HttpResponse  

def emp(request):  
    if request.method == "POST":  
        form = EmployeesForm(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/hello')  
            except:  
                pass  
    else:  
        form = EmployeesForm()  
    return render(request,'index.html',{'form1':form})  



def index1(request):  
    if request.method == 'POST':  
        student = StudentsForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentsForm()  
        return render(request,"index.html",{'form2':student})  