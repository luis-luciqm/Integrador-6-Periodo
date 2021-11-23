from django.urls import path
from .views import *
urlpatterns = [
    path('',AnnouncementListView.as_view(), name="listar_anuncios"),
    path('detalhes_anuncio/<int:pk>/', AnnouncementDatailView.as_view(), name="detalhes_anuncio"),
]