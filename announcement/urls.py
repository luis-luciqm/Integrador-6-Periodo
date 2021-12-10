from django.urls import path
from .views import *
urlpatterns = [
    path('detalhes_anuncio/<slug:slug>/', AnnouncementDatailView.as_view(), name="detalhes_anuncio"),
    path('criar_anuncio/', AnnouncementCreateView.as_view(), name="criar_anuncio"),
    path('seus_anuncios/', AnnouncementYourView.as_view(), name="seus_anuncios"),
    
]