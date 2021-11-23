from django.urls.conf import path
from django.contrib.auth.views import LogoutView
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    # path("login/", auth_views.LoginView.as_view(template_name = "accounts/login.html"), name='login'),
    path('sair/', LogoutView.as_view(), name='sair'),
    path('register/', UserCreateView.as_view(), name='register'),
]
