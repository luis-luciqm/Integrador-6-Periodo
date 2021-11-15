from django.shortcuts import render
from django.views.generic import ListView
from .models import Teste

# Create your views here.

class Teste(ListView):
    template_name = 'teste.html'
    model = Teste
