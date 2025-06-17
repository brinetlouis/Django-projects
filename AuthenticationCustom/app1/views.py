from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from app1.forms import SignupForm
from app1.forms import LoginForm


class SignupView(View):
    def get(self,request):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            # user=form_instance.save(commit=False)
            # user.set_password(form_instance.cleaned_data['password'])
            # user.save()
            form_instance.save()
            return redirect("login")

class HomeView(View):
    def get(self,request):
        return render(request,'home.html')


class LoginView(View):
    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd = form_instance.cleaned_data['password']
            print(name,pwd)
            user=authenticate(username=name,password=pwd)
            if user:
                login(request,user)
                return redirect('home')
            else:
                print("invalid user credentials")
                return redirect('login')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')