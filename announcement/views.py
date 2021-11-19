from django.shortcuts import render
from django.views.generic import ListView

from announcement.models import Announcement
# Create your views here.

class AnnouncementListView(ListView):
    Model = Announcement
    template_name = 'list_announcement.html'
    queryset = Announcement.objects.all()
    context_object_name = 'announces'