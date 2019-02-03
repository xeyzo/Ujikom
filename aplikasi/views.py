from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    return HttpResponse ("Hello world")

@login_required
def home (request):
    return render (request, 'home.html',

    {'title': 'Welcome to homepage'})


def login (request):
    return render (request, 'login.html')
