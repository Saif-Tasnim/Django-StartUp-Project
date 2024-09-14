from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("<h1> this is course page </h1>")

def feedback(request):
    return HttpResponse("<h1> this is feedback page </h1>")

