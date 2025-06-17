from django.shortcuts import render,redirect

from books.forms import Addbook
from books.models import Book

#home
def home(request):
    return render(request,'home.html')

#Addbook
def add_book(request):
    if request.method=="POST":
        print(request.POST)
        print(request.FILES)
        form_instance=Addbook(request.POST,request.FILES)
        if form_instance.is_valid():
            # data=form_instance.cleaned_data
            # print(data)
            # t=data['Title']
            # a=data['Author']
            # p=data['Price']
            # pa=data['Pages']
            # l=data['Language']
            # i=data['Image']
            # b = Book.objects.create(title=t, author=a, price=p, pages=pa, language=l,image=i)
            # b.save()
            form_instance.save()
        return redirect('books:view_book')
    form_instance=Addbook()
    return render(request,'add_book.html',{'form':form_instance})
#viewbook
def view_book(request):
    b=Book.objects.all()
    return render(request,'view_book.html',{'books':b})
def add_book1(request):
    if request.method=="POST":
        print(request.POST)
        print(request.FILES)
        t=request.POST['t']
        a= request.POST['a']
        p= request.POST['p']
        pa = request.POST['pa']
        l = request.POST['l']
        i=request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,image=i)
        b.save()
        return redirect('books:view_book')
    return render(request,'add_book1.html')


def detail(request,i):
    b=Book.objects.get(id=i)
    return render(request,'detail.html',{'book':b})

def edit(request,i):
    b = Book.objects.get(id=i)
    if request.method=="POST":
        form_instance=Addbook(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:view_book')

    form_instance=Addbook(instance=b)
    return render(request, 'edit.html', {'form': form_instance})

def deletebook(request,i):
    b=Book.objects.get(id=i)
    b.delete()
    return redirect('books:view_book')

from django.db.models import Q
def searchbook(request):
    if request.method == "POST":
        data=request.POST['k']
        b=Book.objects.filter(Q(title__contains=data)|Q(author__contains=data)|Q(language__contains=data))
        return render(request, 'search.html', {'book': b})
    return render(request,'search.html')
