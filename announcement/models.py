from django.db import models
from ckeditor.fields import RichTextField
from authentication.models import User
from .utils import *

# Create your models here.
class City (models.Model):
    name = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    class Meta:
        verbose_name = "Cidade"
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=False)
    number_vacancies = models.IntegerField()
    city = models.ForeignKey(City, blank=True, on_delete=models.SET_NULL, related_name="city_announcement", null=True)
    prerequisites = models.TextField()
    note = models.TextField()
    email = models.EmailField()
    image = models.ImageField(upload_to='img/announces/',blank=True,null=True,max_length=255)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_announcement")
    
    slug = models.SlugField(max_length=255, null=False, blank=True, unique=True)
    
    class Meta:
        verbose_name = "Anuncios"
        
    def save(self, *args, **kwargs):    
       
        if self.slug == '' or self.slug == None:
            self.slug = unique_slug_generator(self)

        super().save()
        
