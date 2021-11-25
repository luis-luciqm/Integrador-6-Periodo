from django.http import response
from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import Group


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

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        user = form.save(commit=False)
        # user.is_active=False
        user.save()
        my_group = Group.objects.get(name='Normal') 
        user.groups.add(my_group)
        return super().form_valid(form)