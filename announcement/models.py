from django.db import models
from ckeditor.fields import RichTextField
from authentication.models import User

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=False)
    number_vacancies = models.IntegerField()
    city = models.CharField(max_length=150)
    prerequisites = models.TextField()
    note = models.TextField()
    email = models.EmailField()
    image = models.ImageField(upload_to='img/announces/',blank=True,null=True,max_length=255)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_announcement")
    
    class Meta:
        verbose_name = "Anuncios"