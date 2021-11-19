from rest_framework import serializers
from announcement.models import *

class AnnouncementSereializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('__all__')