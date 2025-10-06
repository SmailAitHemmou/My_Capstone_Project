from django.shortcuts import render

from django.http import HttpResponse

def series(request):
    return HttpResponse("This is The Series Page.")