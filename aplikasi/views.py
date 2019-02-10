from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Pendaftaran, Pembayaran, Pasien


def index (request):
    return HttpResponse ("Hello world")

@login_required
def home (request):
    return render (request, 'home.html',

    {'title': 'Welcome to homepage'})


def login (request):
    return render (request, 'login.html')


def pendaftaran (request):
    pendaftaran = Pendaftaran.objects.all()
    return render(request, 'pendaftaran.html', {'pendaftaran': pendaftaran})


def pembayaran (request):
    pembayaran = Pembayaran.objects.all()
    return render(request, 'pembayaran.html', {'pembayaran': pembayaran})


def pasien (request):
    pasien = Pasien.objects.all()
    return render(request, 'pasien.html', {'pasien': pasien})