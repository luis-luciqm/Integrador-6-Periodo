from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

# Create your models here.

class User(AbstractBaseUser):
    class Meta:
        verbose_name = "usuario"
        
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    password = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/users/',blank=True,null=True,max_length=255)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

