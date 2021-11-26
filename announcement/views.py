from django.db.models import query
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from announcement.models import Announcement, City
from .forms import AnnouncementForm
# Create your views here.

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'list_announcement.html'
    queryset = Announcement.objects.all()
    context_object_name = 'announces'
    
    def get_context_data(self):
        context = super(ListView, self).get_context_data()
        context['citys'] = City.objects.all()
        return context
    def get_queryset(self):
        if self.request.GET.get('search_for_type_vacancies') and self.request.GET.get('search_for_citys'):
            type = self.request.GET.get('search_for_type_vacancies')
            city = self.request.GET.get('search_for_citys')
            announce = Announcement.objects.filter(type_vacancy=type,city__name=city)
            if announce:
                return announce
        elif self.request.GET.get('search_for_type_vacancies'):
            type = self.request.GET.get('search_for_type_vacancies')
            announce = Announcement.objects.filter(type_vacancy=type)
            if announce:
                return announce
            
        elif self.request.GET.get('search_for_citys'):
            city = self.request.GET.get('search_for_citys')
            announce = Announcement.objects.filter(city__name=city)
            if announce:
                return announce
            
        return Announcement.objects.all()
class AnnouncementDatailView(DetailView):
    model = Announcement
    queryset = Announcement.objects.all()
    context_object_name = 'announce'
    lookup_field = 'slug'

class AnnouncementCreateView(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement/form-create-anuncio.html'
    success_url = '/'
    permission_required = ('announcement.add_announcement')
    
    def form_valid(self, form):
        ad = self.object = form.save(commit=False)
        ad.user = self.request.user
        return super().form_valid(form)
    
class AnnouncementYourView(LoginRequiredMixin,ListView):
    model = Announcement
    template_name = 'announcement/your_announces.html'
    context_object_name = 'announces'
    
    def get_queryset(self):
        queryset = Announcement.objects.filter(user = self.request.user)
        return queryset