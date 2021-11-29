from django.contrib.auth.views import LoginView,PasswordResetView
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
        my_group = Group.objects.get(name='Normal') 
        user.groups.add(my_group)
        return super().form_valid(form)
    
class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password-reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    html_email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = '/accounts/password_reset/done/'
    
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