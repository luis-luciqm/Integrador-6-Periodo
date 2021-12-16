from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, Group, PermissionsMixin)

# Create your models here.

class City (models.Model):
    name = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    class Meta:
        verbose_name = "Cidade"

    def __str__(self):
        return self.name + ' / ' + self.estado
class UserManager(BaseUserManager):
    
    def create_user(self, username,email,password=None):
        if username is None:
            raise TypeError('Usuário deve informar o nome')
        if email is None:
            raise TypeError('Users deve informar o Email')
    
        user = self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "usuario"
        
    username = models.CharField(max_length=200, blank=True, unique=True)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/img/',blank=True,null=True,max_length=255)
    
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    city = models.ForeignKey(City,related_name="city_user", null=True, on_delete= models.SET_NULL)
    curriculum = models.FileField(upload_to='users/curriculos/',null=True,max_length=500, blank = True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


