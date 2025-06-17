from django import forms
# class Addbook(forms.Form):
#     Title=forms.CharField()
#     Author=forms.CharField()
#     Price=forms.IntegerField()
#     Pages=forms.IntegerField()
#     Language=forms.CharField()
#     Image=forms.ImageField()

from books.models import Book
class Addbook(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"