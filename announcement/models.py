from django.db import models
from ckeditor.fields import RichTextField
from authentication.models import *
from .utils import *

# Create your models here.
class Announcement(models.Model):
    TYPE_VACANCY = (
        ('emprego', "Emprego"),
        ('estágio', "Estágio")
    )
    
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=False)
    number_vacancies = models.IntegerField()
    city = models.ForeignKey(City, blank=True, on_delete=models.SET_NULL, related_name="city_announcement", null=True)
    email = models.EmailField()
    money = models.IntegerField(default=0)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_announcement")
    
    slug = models.SlugField(max_length=255, null=False, blank=True, unique=True)
    type_vacancy = models.CharField(choices=TYPE_VACANCY, max_length=25, default='1')
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Anuncios"
        
    def save(self, *args, **kwargs):    
       
        if self.slug == '' or self.slug == None:
            self.slug = unique_slug_generator(self)

        super().save()
    
    def __str__(self):
        return self.title

class ParticipateAnnounce(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_partcipate")
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE,related_name="announcement_participate")
    
