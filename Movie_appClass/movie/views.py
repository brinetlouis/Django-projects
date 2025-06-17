from msilib.schema import ListView

from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from movie.forms import MovieForm
from movie.models import Movie
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class HomeView(ListView):
    model=Movie
    template_name = 'movielist.html'
    context_object_name = 'movie'


class AddmovieView(CreateView):
    form_class=MovieForm
    template_name = 'add_movie.html'
    model = Movie
    success_url = reverse_lazy('home')


class DetailView(DetailView):
    model=Movie
    template_name='detail.html'
    context_object_name='movie'


class EditView(UpdateView):
    form_class = MovieForm
    template_name = 'edit.html'
    model = Movie
    success_url = reverse_lazy('home')

class DeleteView(DeleteView):
    model=Movie
    template_name='delete.html'
    success_url=reverse_lazy('home')

