from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import SeriesForm
from .models import Serie

from django.contrib.auth.mixins import LoginRequiredMixin


class SerieList(LoginRequiredMixin, ListView):
    model = Serie
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['series'] = context['series'].filter(user=self.request.user)
        context['count'] = context['series'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['series'] = context['series'].filter(
                name_serie__startswith=search_input)

        context['search_input'] = search_input

        return context

class SerieDetail(LoginRequiredMixin, DetailView):
    model = Serie
    context_object_name = 'serie'
    template_name = 'series/serie_detail.html'

class SerieCreate(LoginRequiredMixin, CreateView):
    model = Serie
    fields = ['name_serie', 'episodes_total', 'episodes_watched', 'release_year', 'description', 'complete']
    success_url = reverse_lazy('series')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SerieCreate, self).form_valid(form)

class SerieUpdate(LoginRequiredMixin, UpdateView):
    model = Serie
    fields = ['name_serie', 'episodes_total', 'episodes_watched', 'release_year', 'description', 'complete']
    success_url = reverse_lazy('series')

class SerieDelete(LoginRequiredMixin, DeleteView):
    model = Serie
    context_object_name = 'serie'
    success_url = reverse_lazy('series')
    template_name = 'series/serie_delete.html'


def add_series(request):
    if request.method == 'POST':
        form = SeriesForm(request.POST)
        if form.is_valid():
            series = form.save(commit=False)

            if request.user.is_authenticated:
                series.user = request.user
            else:
                series.user = User.objects.first()

            series.save()
            return redirect('serie_list')
    else:
        form = SeriesForm()

    return render(request, 'series/serie_form.html', {'form': form})
