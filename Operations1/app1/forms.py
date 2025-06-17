from django import forms
from django.forms import PasswordInput, RadioSelect, ChoiceField, NumberInput


class AdditionForm(forms.Form):
    number1=forms.IntegerField()
    number2=forms.IntegerField()

class Fact(forms.Form):
    number1=forms.IntegerField()

class SignupForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=PasswordInput)
    email=forms.EmailField()
    gender_choices={('male','Male'),('female','Female')}
    gender=forms.ChoiceField(choices=gender_choices,widget=RadioSelect)
    role_choices=[('admin','Admin'),('student','Student')]
    role=forms.ChoiceField(choices=role_choices)

class Calorie(forms.Form):
    gender_choices = {('male', 'Male'), ('female', 'Female')}
    Gender = forms.ChoiceField(choices=gender_choices, widget=RadioSelect,)
    weight=forms.IntegerField()
    height=forms.IntegerField()
    Age=forms.IntegerField()
    activity_choices = [(1.2, 'Sedentary(little/no exercise)'), (1.375, 'Lightly active(exercise 1-3 days/week)'),(1.55,'Moderately active(exercise 3-5 days/week)'),(1.75,'Very active(exercise 6-7 days/week)'),(1.9,'Extra active(very intence activity)')]
    Activity_Level= forms.ChoiceField(choices=activity_choices)