from django import forms
class Bmi(forms.Form):
    number1=forms.IntegerField()
    number2=forms.IntegerField()