from .serializers import *
from rest_framework import generics
from announcement.models import *
from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsUserAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=['admin', 'Empresa']).exists():
            return True
        return False

class AnnouncementListViewSet(generics.ListAPIView):
    serializer_class = AnnouncementSereializer
    def get_queryset(self):    
        queryset = Announcement.objects.all()
        return queryset
    
class AnnouncementCreateViewSet(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,IsUserAdmin)
    serializer_class = AnnouncementSereializer

class AnnouncementListActiveViewSet(generics.ListAPIView):
    serializer_class = AnnouncementSereializer

    def get_queryset(self):
        return Announcement.objects.filter(active = True)


