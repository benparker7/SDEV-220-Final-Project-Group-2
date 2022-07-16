from re import template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from . import util
from .models import Users

# Create your views here.

def index(request):
    return render(request, 'login.html');

def search(request):
    """Search form."""

    keyword = request.GET['keyword']
    if keyword in util.list_entries():
        return redirect('entry_page', entry_name=keyword)
    else:
        context = {
            'search_results': util.search_entry(keyword)
        }
        return render(
            request,
            'encyclopedia/search_results.html',
            context
        )