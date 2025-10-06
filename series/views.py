from django.shortcuts import render

def series(request):
    return render(request, 'series/series.html')