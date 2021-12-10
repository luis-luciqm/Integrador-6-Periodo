from django.db import models

from authentication.models import User

# Create your models here.

class Solicitation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_solicitation")
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    accept = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Solicitações'
        
    def __str__(self):
        return self.user.username