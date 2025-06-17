from django.shortcuts import render
#render used for create webpage responses

#context used to pass data from views to template file.context is a dictionary type.variable containing keys and values

from django.http import HttpResponse
#Home View
def home(request):
    context={'name':'Arun','age':25}
    return render(request,'home.html',context)
#First View
def first(request):
    return render(request,'first.html')
#Second View
def second(request):
    return render(request,'second.html')

