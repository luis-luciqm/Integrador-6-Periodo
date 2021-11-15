from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('teste/', Teste.as_view(), name="teste"),
]