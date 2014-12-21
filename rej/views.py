# _*_ coding: utf-8 _*_
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from rej.models import Persony
from .forms import FormularzRejestracji
from datetime import datetime
import re


def wybor_person():
    zmieniaj = Persony.objects.order_by('username')
    a = int(datetime.now().year)
    krot = []
    for zz in zmieniaj:
        if zz.id <> 0:
            roki = str(a - int(zz.birthday.year))
            krot.append(re.split(' ',zz.username)[0] + ' (' + roki + ' lat)' )
    return krot


def stary(): # wyszukanie mlodych i starych 
    a = int(datetime.now().year)
    wiek = Persony.objects.order_by('birthday')
    krota = "Najstarszy jest " + re.split(' ', wiek.first().username)[0] + " (" + str(a - wiek.first().birthday.year) + "), a najmlodszy " + re.split(' ', wiek.last().username)[0] + " (" + str(a - wiek.last().birthday.year) + ")."
    return krota


def register_page(request):
    if request.method == 'POST':
        form = FormularzRejestracji(request.POST)
        if form.is_valid():
            a = int(datetime.now().year)
            b = int(form.cleaned_data['birthday'].year)
            lata = (a - b)
            wiekowo = 1
            if lata < 18:
                wiekowo = 0
            user = Persony.objects.create(
              username=form.cleaned_data['username'],
              birthday=form.cleaned_data['birthday'],
              parents=form.cleaned_data['parents'],
              adult = wiekowo
            )
            user.save()
            template = get_template("rej/rejestr_success.html")
            variables = RequestContext(request,{'username':form.cleaned_data['username']})
            output = template.render(variables)
            return HttpResponse(output)            
    else:
        form = FormularzRejestracji()
    template = get_template("rej/rejestr.html")    
    variables = RequestContext(request,{'form':form, 'tup':wybor_person(), 'mlody': stary()})
    output = template.render(variables)
    return HttpResponse(output)




################
