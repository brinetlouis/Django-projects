from django.shortcuts import render
from app1.forms import Bmi
def bmi(request):
    if request.method=="POST":
        print(request.POST)
        return render(request,'bmivalue.html')
    form_instance=Bmi()
    return render(request,'bmivalue.html',{'form':form_instance})
