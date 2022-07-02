from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Users

# Create your views here.

def index(request):
    return render(request, 'login.html');

