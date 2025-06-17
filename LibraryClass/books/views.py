from django.shortcuts import render,redirect

from books.forms import Addbook
from books.models import Book

#home
from django.views import View
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")


#Addbook
class AddbookView(View):
    def get(self,request,*args,**kwargs):
        form_instance = Addbook()
        return render(request, 'add_book.html', {'form': form_instance})
    def post(self,request,*args,**kwargs):
        form_instance = Addbook(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:view_book')


#viewbook
class ViewbookView(View):
    def get(self,request,*args,**kwargs):
        b = Book.objects.all()
        return render(request, 'view_book.html', {'books': b})


class AddbookView1(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'add_book1.html')
    def post(self,request,*args,**kwargs):
        t = request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        pa = request.POST['pa']
        l = request.POST['l']
        i = request.FILES['i']
        b = Book.objects.create(title=t, author=a, price=p, pages=pa, language=l, image=i)
        b.save()
        return redirect('books:view_book')






class DetailView(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        return render(request, 'detail.html', {'book': b})


class EditView(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        form_instance = Addbook(instance=b)
        return render(request, 'edit.html', {'form': form_instance})
    def post(self,request,i):
        b = Book.objects.get(id=i)
        form_instance = Addbook(request.POST, request.FILES, instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:view_book')




class DeletebookView(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        b.delete()
        return redirect('books:view_book')




from django.db.models import Q
class SearchbookView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'search.html')
    def post(self,request,*args,**kwargs):
        data = request.POST['k']
        b = Book.objects.filter(Q(title__contains=data) | Q(author__contains=data) | Q(language__contains=data))
        return render(request, 'search.html', {'book': b})


