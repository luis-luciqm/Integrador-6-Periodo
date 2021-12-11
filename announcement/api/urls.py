from django.urls import path
from .viewsets import *

urlpatterns = [
    path('', AnnouncementListViewSet.as_view(), name=''),
    path('listar_anuncios_ativos/', AnnouncementListActiveViewSet.as_view(), name='listar_anuncios_ativos'),
    path('criar_anuncio/', AnnouncementCreateViewSet.as_view(), name='criar_anuncios'),
]