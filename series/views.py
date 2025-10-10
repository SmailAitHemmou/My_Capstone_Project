from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import SeriesForm
from .models import Serie


class SerieList(ListView):
    model = Serie
    context_object_name = 'series'

class SerieDetail(DetailView):
    model = Serie
    context_object_name = 'serie'
    template_name = 'series/serie_detail.html'

class SerieCreate(CreateView):
    model = Serie
    fields = '__all__'
    success_url = reverse_lazy('series')

class SerieUpdate(UpdateView):
    model = Serie
    fields = '__all__'
    success_url = reverse_lazy('series')

class SerieDelete(DeleteView):
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
