from django.urls import path
from .views import *
urlpatterns = [
    path('detalhes_anuncio/<slug:slug>/', AnnouncementDatailView.as_view(), name="detalhes_anuncio"),
    path('criar_anuncio/', AnnouncementCreateView.as_view(), name="criar_anuncio"),
    path('seus_anuncios/', AnnouncementYourView.as_view(), name="seus_anuncios"),
    path('editar_anuncio/<slug:slug>/', AnnouncementUpdateView.as_view(), name="editar_anuncio"),
    path('vagas_empregos/', AnnouncementListAllJobsViewSet.as_view(), name="vagas_empregos"),
    path('vagas_estagio/', AnnouncementListAllPhasesViewSet.as_view(), name='vagas_estagio'),
    path('listagem_pela_empresa/<int:id>/', AnnouncementListByCompanyViewSet.as_view(), name='listagem_pela_empresa'),
    path('ativar_anuncio/<slug:slug>/', AnnouncementEnableView.as_view(), name='ativar_anuncio'),
    path('desativar_anuncio/<slug:slug>/', AnnouncementDisableView.as_view(), name="desativar_anuncio"),
    #path('todas_as_vagas/', AnnouncementListAllVacanciesViewSet.as_view(), name="todas_as_vagas"),
    path('search/', search_auto_complete),
    path('search_phases/', search_auto_complete_phases),
    path('search_jobs/', search_auto_complete_jobs),
    path('search_company/', search_auto_complete_company),
    path('candidatos/<slug:slug>/',ParticipateAnnounceList.as_view(), name="candidatos"),

    
]