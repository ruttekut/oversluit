# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/home.html',  {'nbar': 'home'})


def calculation(request):
    return render(request, 'home/berekening.html', {'nbar': 'bereken'})


def contact(request):
    return render(request, 'home/contact.html', {'nbar': 'contact'})
