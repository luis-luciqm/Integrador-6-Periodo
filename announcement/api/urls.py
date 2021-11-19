from django.urls import path
from .viewsets import *

urlpatterns = [
    path('listar_anuncios/', AnnouncementListViewSet.as_view(), name='listar_anuncios'),
    path('criar_anuncio/', AnnouncementCreateViewSet.as_view(), name='criar_anuncios'),
]