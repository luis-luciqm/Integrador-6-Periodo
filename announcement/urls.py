from django.urls import path
from .views import *
urlpatterns = [
    path('',AnnouncementListView.as_view(), name="listar_anuncios"),
    
]