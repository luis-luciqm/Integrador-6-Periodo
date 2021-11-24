from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView

from announcement.models import Announcement
from .forms import AnnouncementForm
# Create your views here.

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'list_announcement.html'
    queryset = Announcement.objects.all()
    context_object_name = 'announces'
    
class AnnouncementDatailView(DetailView):
    model = Announcement
    queryset = Announcement.objects.all()
    context_object_name = 'announce'

class AnnouncementCreateView(CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement/form-create-anuncio.html'
    success_url = '/'
    
    def form_valid(self, form):
        ad = self.object = form.save(commit=False)
        ad.user = self.request.user
        return super().form_valid(form)