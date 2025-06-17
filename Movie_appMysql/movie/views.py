from django.shortcuts import render,redirect
from movie.forms import MovieForm
from movie.models import Movie
def home(request):
    m = Movie.objects.all()
    return render(request,"movielist.html",{'movie':m})
def add_movie(request):
    if request.method=='POST':
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')
    form_instance=MovieForm()
    return render(request,"add_movie.html",{'form':form_instance})


def detail(request,i):
    m = Movie.objects.get(id=i)
    return render(request,'detail.html',{'movie':m})

def deletemovie(request,i):
    m=Movie.objects.get(id=i)
    m.delete()
    return redirect('home')

def edit(request,i):
    m = Movie.objects.get(id=i)
    if request.method=="POST":
        form_instance=MovieForm(request.POST,request.FILES,instance=m)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')

    form_instance=MovieForm(instance=m)
    return render(request, 'edit.html', {'form': form_instance})