from django import forms


class Berekening(forms.Form):
    """Form: the calculationForm"""
    BKR = (
        ('nee', 'Geen bkr codering'),
        ('ja', 'Wel een bkr codering'),
        ('hersteld', 'Ja, hersteld'),
    )
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    adress = forms.CharField(max_length=250)
    homeNumber = forms.CharField(max_length=8)
    zipcode = forms.CharField(max_length=8)
    income = forms.IntegerField()
    income_partner = forms.IntegerField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    bkr = forms.CharField(max_length=8)
