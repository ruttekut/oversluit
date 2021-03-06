# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


# Create your models here.
class Leads(models.Model):
    BKR = (
        ('nee', 'Geen bkr codering'),
        ('ja', 'Wel een bkr codering'),
        ('hersteld', 'Ja, hersteld'),
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    adress = models.CharField(max_length=250)
    home_number = models.CharField(max_length=8, null=True)
    zipcode = models.CharField(max_length=8)
    income = models.IntegerField()
    income_partner = models.IntegerField(blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    bkr = models.CharField(max_length=8, choices=BKR)
    calculationDate = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = "leads"

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
