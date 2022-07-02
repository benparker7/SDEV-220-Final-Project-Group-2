from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    page = "<html><head><title>Home Page</title></head><body><h1>Hello</h1> <li><a href='/login'>Login</li></html>"
    return HttpResponse(page)
