
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
from django.http import JsonResponse
# Create your views here.
from django.views import View
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
        context['tot_announces_emprego'] = 0
        context['tot_announces_estagio'] = 0
        context['announces_estagio'] = Announcement.objects.filter(type_vacancy = 'estágio',active = True)
        context['announces_emprego'] = Announcement.objects.filter(type_vacancy = 'emprego',active = True)
        for t in context['announces_estagio']:
            context['tot_announces_estagio'] += t.number_vacancies
        
        for t in context['announces_emprego']:
            context['tot_announces_emprego'] += t.number_vacancies
        context['last_posts'] = Announcement.objects.filter(active = True).order_by('-created')[:8]
        context['tot_users'] = User.objects.all().count()
        context['tot_empresas'] = User.objects.filter(groups__name__in=['Empresa']).count()
        
        if self.request.user.username: #necessita do usuario está logado
            if self.request.user.groups.filter(name = 'admin'):
                context['notifications_solicitation'] = Notification.objects.filter(participate = None, solicitation__accept = False).order_by('-created')[:4]
            context['notifications_partipate'] = Notification.objects.filter(solicitation = None, participate__announcement__user = self.request.user, created__date = datetime.date.today()).order_by('-created')[:4]
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
    permission_required = ('announcement.add_announcement')
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

class AnnouncementListAllVacanciesViewSet(ListView):
    model = Announcement
    template_name = 'announcement/all_vacancies.html'
    paginate_by = 16
    
    def get_queryset(self):
        retorno = None
        if self.request.GET.get('search'):
            retorno = Announcement.objects.filter(Q(city__name = self.request.GET.get('search')) | Q(type_vacancy =self.request.GET.get('search') ) | Q(title__icontains = self.request.GET.get('search'))).order_by('-created')
        else:
            retorno = Announcement.objects.filter(active = True).order_by('-created')
        return retorno
    
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        if self.request.GET.get('search'):
            context['definerouter'] = self.request.GET.get('search')
        return context

class AnnouncementListAllPhasesViewSet(ListView): # phases = estágios
    model = Announcement
    template_name = 'announcement/phases.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['phases'] = Announcement.objects.filter(type_vacancy = 'estágio').filter(active = True).order_by('-created')
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
                if not request.user.curriculum:
                    messages.warning(request, "Para maiores chances de conseguir uma vaga, vá até a seção de editar perfil e anexe seu currículo.")
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
        anuncio.created = datetime.datetime.today()
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

def search_auto_complete(request):
    value = request.GET.get('city')
    payload = []
    if value:
        citys = City.objects.filter(name__icontains = value)
        announces = Announcement.objects.filter(title__icontains = value)
        types = Announcement.objects.filter(type_vacancy__icontains = value)
        # companys = User.objects.filter(username__icontains = value)
        
        for city in citys:
            payload.append(city.name)
            
        for annouce in announces:
            payload.append(annouce.title)
            
        for type_v in types:
            payload.append(type_v.type_vacancy)

        # for company in companys:
        #     payload.append(company.fullname)

    return JsonResponse({'status': 200, 'data': payload})

class AboutUs(View):
    template_name = 'announcement/about-us.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    
class ParticipateAnnounceList(LoginRequiredMixin, ListView):
    model = ParticipateAnnounce
    template_name = 'announcement/candidatos-anounce.html'
    paginate_by = 15
    
    def get_queryset(self):
        return ParticipateAnnounce.objects.filter(announcement__slug = self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qtd_participates'] = ParticipateAnnounce.objects.filter(announcement__slug = self.kwargs['slug']).count()
        return context
