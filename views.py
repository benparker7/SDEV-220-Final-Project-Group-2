from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    page = "<html><head><title>test page</title></head><body><h1>Hello</h1></html>"
    return HttpResponse(page)
