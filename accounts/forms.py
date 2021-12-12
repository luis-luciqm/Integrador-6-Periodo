from django import forms
from django.forms.fields import ImageField
from authentication.models import City, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *


class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'username','fullname', 'city', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

    # Header Image Field
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['fullname'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        
        
class SolicitationForm(forms.ModelForm):
    description = forms.CharField()
    class Meta:
        model = Solicitation
        fields = ['description']
        
        
class UserForm2(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField()
    fullname = forms.CharField()
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False)
    image= forms.ImageField()
    curriculum = forms.FileField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'username','fullname', 'city', 'image', 'curriculum']
        
# class PasswordResetForm():