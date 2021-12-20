"""integrador_6_periodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth import views as auth_views

from announcement.views import AnnouncementListView
schema_view = get_swagger_view(title='RN Empregos')
# from account.views import AccountList
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/autenticacao/', include('authentication.urls')),
    path('anuncio/', include('announcement.urls')),
    path('', AnnouncementListView.as_view(), name="listar_anuncios"),
    path('api/', schema_view, name='schema-swagger-ui'),
    path('api/anuncio/', include('announcement.api.urls')),
    path('api/accounts/', include('accounts.api.urls')),
    path('accounts/', include('accounts.urls')),
    
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
