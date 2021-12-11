
from django.contrib import messages
from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import UpdateView

from announcement.models import Announcement, City, ParticipateAnnounce
from authentication.models import User
from .forms import AnnouncementForm
# Create your views here.

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'list_announcement.html'
    queryset = Announcement.objects.filter(Q(type_vacancy = 'emprego') | Q(type_vacancy = 'estagio')).filter(active = True)[:4]
    context_object_name = 'announcements'
    
    def get_context_data(self):
        context = super(ListView, self).get_context_data()
        context['citys'] = City.objects.all()
        context['announces_estagio'] = Announcement.objects.filter(type_vacancy = 'estagio').filter(active = True).count()
        context['announces_emprego'] = Announcement.objects.filter(type_vacancy = 'emprego').filter(active = True).count()
        context['last_posts'] = Announcement.objects.filter(active = True).order_by('-created')[:7]
        context['tot_users'] = User.objects.all().count()
        context['tot_empresas'] = User.objects.filter(groups__name__in=['Empresa']).count()
        
        return context
    

class AnnouncementDatailView(DetailView):
    model = Announcement
    queryset = Announcement.objects.all()
    context_object_name = 'announce'
    lookup_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anuncio'] = Announcement.objects.get(slug = self.kwargs['slug'])
        return context


class AnnouncementCreateView(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement/form-create-anuncio.html'
    success_url = '/'
    permission_required = ('announcement.add_announcement')
    
    def form_valid(self, form):
        ad = self.object = form.save(commit=False)
        ad.user = self.request.user
        ad.email = self.request.user.email
        return super().form_valid(form)

class AnnouncementUpdateView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement/form-create-anuncio.html'
    success_url = '/'
    permission_required = ('announcement.change_announcement')
    queryset = Announcement.objects.all()
    lookup_field = 'slug'

class AnnouncementYourView(LoginRequiredMixin,ListView):
    model = Announcement
    template_name = 'announcement/your_announces.html'
    context_object_name = 'announces'
    
    def get_queryset(self):
        queryset = Announcement.objects.filter(user = self.request.user)
        return queryset
    
def ParticipateAnnounceFun(request, pk):
    anounce = Announcement.objects.get(pk=pk)
    if not ParticipateAnnounce.objects.filter(user = request.user, announcement_id = pk).exists():
        ParticipateAnnounce.objects.create(user = request.user, announcement = anounce)
    else:
        messages.error(request, "Você ja se candidatou a está vaga")
    return redirect(f'/anuncio/detalhes_anuncio/{anounce.slug}')