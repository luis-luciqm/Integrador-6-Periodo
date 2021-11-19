from .serializers import *
from rest_framework import generics
from announcement.models import *

class AnnouncementListViewSet(generics.ListAPIView):
    serializer_class = AnnouncementSereializer
    def get_queryset(self):    
        queryset = Announcement.objects.all()
        return queryset
    
class AnnouncementCreateViewSet(generics.CreateAPIView):
    serializer_class = AnnouncementSereializer
    