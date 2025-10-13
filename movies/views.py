from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie

from django.contrib.auth.mixins import LoginRequiredMixin


class MovieList(LoginRequiredMixin, ListView):
    model = Movie
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = context['movies'].filter(user=self.request.user)
        context['count'] = context['movies'].filter(complete=False).count()
        return context

class MovieDetail(LoginRequiredMixin, DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movies/movie_detail.html'

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['name_movie', 'release_year', 'description', 'complete']
    success_url = reverse_lazy('movies')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreate, self).form_valid(form)

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['name_movie', 'release_year', 'description', 'complete']
    success_url = reverse_lazy('movies')

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    context_object_name = 'movie'
    success_url = reverse_lazy('movies')
    template_name = 'movies/movie_delete.html'

