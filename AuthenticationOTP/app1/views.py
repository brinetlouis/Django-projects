from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from app1.forms import SignupForm
from app1.forms import LoginForm
from app1.models import User
from django.core.mail import send_mail
from django.contrib import messages

class SignupView(View):
    def get(self,request):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            user=form_instance.save(commit=False)
            user.is_active=False
            user.save()
            user.generate_otp()
            send_mail(
                "Django Auth OTP",
                user.otp,
                "brinetlouis@gamil.com",
                [user.email],
                fail_silently=False,
            )
            return redirect("otp")

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
            user=authenticate(username=name,password=pwd)
            if user and user.is_superuser==True:
                login(request,user)
                return redirect('admin')
            elif user and user.role=='student':
                login(request, user)
                return redirect('student')
            elif user and user.role=='teacher':
                login(request, user)
                return redirect('teacher')
            else:
                print("invalid user credentials")
                return redirect('signin')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home')

    def post(self,request):
        logout(request)
        return redirect('home')

class OtpView(View):
    def get(self,request):
        return render(request, 'otp.html', )
    def post(self,request):
        otp=request.POST['otp']
        try:
            u=User.objects.get(otp=otp)
            u.is_active=True
            u.is_verified=True
            u.save()
            return redirect('signin')
        except:
            messages.error(request,"Invalid OTP")
            return redirect('otp')


class StudentHomeView(View):
    def get(self,request):
        return render(request,'student.html')

class TeacherHomeView(View):
    def get(self,request):
        return render(request,'teacher.html')

class AdminHomeView(View):
    def get(self,request):
        return render(request,'admin.html')