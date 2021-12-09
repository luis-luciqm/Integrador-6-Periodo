
from django.db.models.query_utils import Q
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
    queryset = Announcement.objects.filter(Q(type_vacancy = 'emprego') | Q(type_vacancy = 'estagio'))[:4]
    context_object_name = 'announcements'
    
    def get_context_data(self):
        context = super(ListView, self).get_context_data()
        context['citys'] = City.objects.all()
        context['announces_estagio'] = Announcement.objects.filter(type_vacancy = 'estagio').count()
        context['announces_emprego'] = Announcement.objects.filter(type_vacancy = 'emprego').count()
        context['last_posts'] = Announcement.objects.all().order_by('-created')[:7]
        
        return context
    

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