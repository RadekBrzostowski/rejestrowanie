# _*_ coding: utf-8 _*_
import re
from django import forms
from .models import Persony
from django.core.exceptions import ObjectDoesNotExist
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime


def wybor():
    zmieniaj = Persony.objects.filter(adult = True).order_by('username')
    krot = [(0, '')]
    for zz in zmieniaj:
        krot.append((zz.id, zz.username))
    return krot


class FormularzRejestracji(forms.Form):
    wybor()
    username = forms.CharField(label="Imie i Nazwisko:",max_length=30)
    birthday = forms.DateTimeField(label="Data urodzenia", widget=SelectDateWidget(years=range(1950,2018)))
    parents = forms.ChoiceField(label="Rodzic", choices=wybor())


    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'\s',username):
            raise forms.ValidationError("Imie i Nazwisko przedzielone spacja!!")
        try:
            Persony.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Taki użytkownik już istnieje")


    def clean_parents(self):
        parents = self.cleaned_data['parents']
        a = int(datetime.now().year)
        b = int(self.cleaned_data['birthday'].year)
        lata = (a - b)
        if (lata < 18) and (parents == ''):
            raise forms.ValidationError("Musisz podac rodzica z listy")
        return parents



