from django.contrib.auth.views import LoginView,PasswordResetView
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView


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
        my_group, created = Group.objects.get_or_create(name='Normal') 
        user.groups.add(my_group)
        return super().form_valid(form)
    
class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password-reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    html_email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = '/accounts/password_reset/done'
    
    def form_valid(self, form):
        #objects
        email = User.objects.filter(email = form.cleaned_data['email']).exists()
        if not email:
            messages.error(self.request, 'Email não consta em nossa base')
            return redirect('/accounts/password_reset/')
        
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)
        
    
class PasswordResetDone(SuccessMessageMixin, PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = '/accounts/login'


class PasswordResetCompleteView(SuccessMessageMixin, PasswordResetCompleteView):
    success_message = 'Senha Alterada com sucesso!'
    template_name = 'accounts/login.html'
    
    
# class PasswordChange(SuccessMessageMixin, PasswordChangeView):
#     template_name = 'accounts/password-change.html'
#     success_url = 'index'
#     success_message = "Senha alterada com sucesso!"