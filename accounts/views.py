from django.http import response
from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib import messages
from .forms import *


class UserLogin(LoginView):
    template_name = 'accounts/login.html'
    success_url = '/'

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possível fazer o login, verifique os dados.')
        return super().form_invalid(form)
    
class UserCreateView(CreateView):
    template_name= 'accounts/auth-register.html'
    form_class = UserForm
    success_url = '/accounts/login'
    success_message = "Usuário Cadastrado! Solicite o administrador a liberação."

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        user = form.save(commit=False)
        user.is_active=False
        user.save()
      
        return super().form_valid(form)