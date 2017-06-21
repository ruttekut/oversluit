from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Leads
from crispy_forms.helper import FormHelper


class Berekening(ModelForm):
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
        labels = {
            'first_name': _('Voornaam'),
            'last_name': _('Achternaam'),
            'adress': _('Adres'),
            'home_number': _('Huisnummer'),
            'zipcode': _('Postcode'),
            'income': _('Inkomen'),
            'income_partner': _('Inkomen partner (optioneel)'),
            'email': _('Emailadres'),
            'phone': _('Mobiele telefoon'),

        }
