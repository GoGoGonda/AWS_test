from django.shortcuts import render
from django.http import HttpResponse

def index(requeset):
    return HttpResponse('Hello Mou')
# Create your views here.
