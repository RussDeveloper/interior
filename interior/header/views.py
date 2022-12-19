from django.shortcuts import render
from django.http import request
from header.models import *

# Create your views here.
def index(request):
    partners = Partners.objects.all()

    return render(request, 'header/index.html', {'partners': partners})

def service(request):
    return render(request, 'header/service.html',)

def about(request):
    return render(request, 'header/about.html',)

def team(request):
    return render(request, 'header/team.html',)

def portfolio(request):
    return render(request, 'header/portfolio_v1.html',)

def blog(request):
    return render(request, 'header/blog.html',)

def testing(request):
    users = Partners.objects.all();
    return render(request, 'header/testing.html', {'users': users})









