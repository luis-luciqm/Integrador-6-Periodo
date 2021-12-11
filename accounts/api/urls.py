from django.urls import path
from .viewsets import *

urlpatterns = [
    path('listar_empresas/', CompanyListViewSet.as_view(), name='listar_empresas'),
    path('criar_empresa/', CompanyCreateViewSet.as_view(), name='criar_empresa'),
]