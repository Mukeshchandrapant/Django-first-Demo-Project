from django.shortcuts import render
from django.http import HttpResponse
from . import views

# Create your views here.


def index(request):
    return HttpResponse("Hey there, this is my first test app!!!")
