from django.shortcuts import render
from django.http import HttpResponse

def movies(request):
    return HttpResponse("This is The Movies Page.")
