from django import forms
from django.contrib.auth.forms import UserCreationForm
from app1.models import User
from django.forms import PasswordInput


# class SignupForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username','password','email','first_name','last_name']

class SignupForm(UserCreationForm):
    role_choices=[('student','Student'),('teacher','Teacher')]
    role=forms.ChoiceField(choices=role_choices,widget=forms.Select)
    class Meta:
        model=User
        fields=['username','password1','password2','phone','email','first_name','last_name','address','role']


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=PasswordInput)
