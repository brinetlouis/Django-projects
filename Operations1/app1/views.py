from django.shortcuts import render
from app1.forms import AdditionForm
from app1.forms import Fact
from app1.forms import SignupForm
from app1.forms import Calorie
def addition(request):
    if request.method=="POST":
        print(request.POST)
        return render(request,'addition.html')

    form_instance=AdditionForm()
    return render(request, 'addition.html',{'form':form_instance})


def fact(request):
    if request.method=="POST":
        print(request.POST)
        return render(request,'factorial.html')
    form_instance=Fact()
    return render(request,'factorial.html',{'form':form_instance})


def signup(request):
    form_instance = SignupForm()
    return render(request,'signup.html',{'form':form_instance})

def calorie(request):
    if request.method=='POST':
        print(request.POST)
        #creating form object using data submitted by user
        form_instance=Calorie(request.POST)
        #checks the validity of data using is_valid()
        if form_instance.is_valid():
            #accessing the cleaned data after validation
            data=form_instance.cleaned_data
            print(data)
            w=data['weight']
            h=data['height']
            a=data['Age']
            g=data['Gender']
            al=data['Activity_Level']
            print(w,h,a,g,al)
            if g=="male":
                bmr=10*w+6.25*h-5*a+5
                cc=bmr*float(al)
            if g=="female":
                bmr=10*w+6.25*h-5*a-161
                cc=bmr*float(al)
            result=cc
            context={'form': form_instance,'result':result}
        return render(request, 'calorie.html',context)
    form_instance = Calorie()
    return render(request, 'calorie.html', {'form': form_instance})