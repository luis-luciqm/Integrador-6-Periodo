from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.detail import DetailView

from announcement.models import Announcement
# Create your views here.

class AnnouncementListView(ListView):
    Model = Announcement
    template_name = 'list_announcement.html'
    queryset = Announcement.objects.all()
    context_object_name = 'announces'
    
class AnnouncementDatailView(DetailView):
    Model = Announcement
    queryset = Announcement.objects.all()
    context_object_name = 'announce'