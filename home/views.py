# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Leads
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    return render(request, 'home/home.html',  {'nbar': 'home'})


def calculation(request):
    return render(request, 'home/berekening.html', {'nbar': 'bereken'})


def contact(request):
    return render(request, 'home/contact.html', {'nbar': 'contact'})


class CreateLead(CreateView):
    """
    Class based view for submitting the calculation form.
    """
    model = Leads
    template_name = 'home/leads_form.html'
    fields = [
        'first_name',
        'last_name',
        'adress',
        'homeNumber',
        'zipcode',
        'income',
        'income_partner',
        'email',
        'phone',
        'bkr'
    ]

    def get_success_url(self):
        return reverse('home:index')
