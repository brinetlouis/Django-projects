from django.db.models.fields import return_None
from django.shortcuts import render,redirect
from app1.forms import Employeeform
from app1.models import Employee
def view(request):
    e=Employee.objects.all()
    return render(request,"home.html",{'employee':e})

def add(request):
    if request.method=="POST":
        form_instance=Employeeform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')
    form_instance=Employeeform
    return render(request,'add.html',{'form':form_instance})

def details(request,i):
    e=Employee.objects.get(id=i)
    return  render(request,'details.html',{'employee':e})

def edit(request,i):
    e=Employee.objects.get(id=i)
    if request.method == "POST":
        form_instance = Employeeform(request.POST, request.FILES,instance=e)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')
    form_instance = Employeeform(instance=e)
    return  render(request,'edit.html',{'form':form_instance})

def deleteuser(request,i):
    e = Employee.objects.get(id=i)
    e.delete()
    return redirect('home')