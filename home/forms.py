from django import forms
from .models import Leads
from crispy_forms.helper import FormHelper


class Berekening(forms.ModelForm):
    """Form: the calculationForm"""
    helper = FormHelper()

    class Meta:
        model = Leads
        fields = [
            'first_name',
            'last_name',
            'adress',
            'home_number',
            'zipcode',
            'income',
            'income_partner',
            'email',
            'phone',
            'bkr'
        ]
