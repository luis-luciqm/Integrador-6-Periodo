from django.db import models

from authentication.models import User
from announcement.models import Announcement, ParticipateAnnounce

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
    
    
class  Notification(models.Model):
    participate = models.ForeignKey(ParticipateAnnounce, on_delete=models.CASCADE, related_name='participate_notification', null=True, blank=True)
    solicitation = models.ForeignKey(Solicitation, on_delete=models.CASCADE, related_name="solicitation_notification", null=True, blank=True)
    text = models.CharField(max_length=150, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text