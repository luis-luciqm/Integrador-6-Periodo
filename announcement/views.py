
from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.shortcuts import redirect
from accounts.models import Notification
from announcement.models import Announcement, City, ParticipateAnnounce
from authentication.models import User
from .forms import AnnouncementForm
from django.urls.base import reverse_lazy
import datetime
# Create your views here.
class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'list_announcement.html'
    context_object_name = 'announcements'

    def get_queryset(self):
        queryset = Announcement.objects.all().order_by('-created')[:6]
        return queryset
    
    def get_context_data(self):
        context = super(ListView, self).get_context_data()
        context['citys'] = City.objects.all()
        context['announces_estagio'] = Announcement.objects.filter(type_vacancy = 'estagio',active = True).count()
        context['announces_emprego'] = Announcement.objects.filter(type_vacancy = 'emprego',active = True).count()
        context['last_posts'] = Announcement.objects.filter(active = True).order_by('-created')[:8]
        context['tot_users'] = User.objects.all().count()
        context['tot_empresas'] = User.objects.filter(groups__name__in=['Empresa']).count()
        
        if self.request.user.username: #necessita do usuario está logado
            if self.request.user.groups.filter(name = 'admin'):
                context['notifications_solicitation'] = Notification.objects.filter(participate = None, solicitation__accept = False).order_by('-created')
            context['notifications_partipate'] = Notification.objects.filter(solicitation = None, participate__announcement__user = self.request.user, created__date = datetime.date.today()).order_by('-created') 
            context['announcements_city'] = Announcement.objects.filter(active = True, city = self.request.user.city).order_by('-created')[:6]    
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
    permission_required = ('announcement.change_announcement')
    queryset = Announcement.objects.all()
    lookup_field = 'slug'
    
    def get_success_url(self,**kwargs):
        messages.success(self.request,f'Anuncio ({self.kwargs["slug"]}) editado com sucesso!')
        return reverse_lazy('seus_anuncios')
        

class AnnouncementYourView(LoginRequiredMixin,ListView):
    model = Announcement
    template_name = 'announcement/your_announces.html'
    context_object_name = 'announces'
    
    def get_queryset(self):
        queryset = Announcement.objects.filter(user = self.request.user)
        return queryset

class AnnouncementListAllJobsViewSet(ListView):
    model = Announcement
    template_name = 'announcement/jobs.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data()
        context['jobs'] = Announcement.objects.filter(type_vacancy = 'emprego').filter(active = True).order_by('-created')
        return context

class AnnouncementListAllPhasesViewSet(ListView): # phases = estágios
    model = Announcement
    template_name = 'announcement/phases.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['phases'] = Announcement.objects.filter(type_vacancy = 'estagio').filter(active = True).order_by('-created')
        return context

class AnnouncementListByCompanyViewSet(ListView):
    model = Announcement
    template_name = 'announcement/list_anuncios_by_company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anuncios_company'] = Announcement.objects.filter(user = self.kwargs['id']).order_by('-created')
        context['user_company'] = User.objects.get(id = self.kwargs['id'])
        return context
    
def ParticipateAnnounceFun(request, pk):
    anounce = Announcement.objects.get(pk=pk)
    if request.user.is_authenticated:
        if not ParticipateAnnounce.objects.filter(user = request.user, announcement_id = pk).exists():
            if not anounce.user == request.user:
                p = ParticipateAnnounce.objects.create(user = request.user, announcement = anounce)
                messages.success(request, "Você agora está concorrendo a vaga. Boa sorte!!")
                Notification.objects.create(participate=p, text=f'Uma nova pessoa se candidatou para o anuncio: {anounce.title}')
            else:
                messages.error(request, "Você não pode se candidatar há uma vaga que você mesmo criou.")
        else:
            messages.error(request, "Você ja se candidatou a esta vaga.")
        return redirect(f'/anuncio/detalhes_anuncio/{anounce.slug}')
    else:
        return redirect(f'/accounts/login/?next=/anuncio/detalhes_anuncio/{anounce.slug}')

class AnnouncementEnableView(LoginRequiredMixin, ListView):
    template_name = 'announcement/announcement_detail.html'
    context_object_name = 'queryset'

    def get_queryset(self):
        anuncio = Announcement.objects.get(slug = self.kwargs['slug'])
        anuncio.active = True
        anuncio.save()
        return anuncio
    
    def get_context_data(self, **kwargs):
        anuncio = Announcement.objects.get(slug = self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        context['anuncio'] = anuncio
        return context

class AnnouncementDisableView(LoginRequiredMixin, ListView):
    template_name = 'announcement/announcement_detail.html'
    context_object_name = 'queryset'
    def get_queryset(self):
        anuncio = Announcement.objects.get(slug = self.kwargs['slug'])
        anuncio.active = False
        anuncio.save()
        return anuncio
    
    def get_context_data(self, **kwargs):
        anuncio = Announcement.objects.get(slug = self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        context['anuncio'] = anuncio
        return context
