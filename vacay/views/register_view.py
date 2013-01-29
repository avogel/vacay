from django import forms
from vacay.forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/home/")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {'form': form,})