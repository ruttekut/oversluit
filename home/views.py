# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import Berekening


# Create your views here.
def index(request):
    return render(request, 'home/home.html',  {'nbar': 'home'})


def calculation(request):
    return render(request, 'home/berekening.html', {'nbar': 'bereken'})


def contact(request):
    return render(request, 'home/contact.html', {'nbar': 'contact'})


def createlead(request):
    if request.method == 'POST':
        form = Berekening(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/berekeninggemaakt.html')
    else:
        form = Berekening()

    return render(request, 'home/berekening.html', {'form': form})
