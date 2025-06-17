from django import forms
from django.contrib.auth.forms import UserCreationForm
from app1.models import User
# class SignupForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username','password','email','first_name','last_name']

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','phone','address','email','first_name','last_name']


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()