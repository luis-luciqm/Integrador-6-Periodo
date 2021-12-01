from django.urls.conf import path
from django.contrib.auth.views import LogoutView
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    # path("login/", auth_views.LoginView.as_view(template_name = "accounts/login.html"), name='login'),
    path('sair/', LogoutView.as_view(), name='sair'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('teste/', PasswordResetView.as_view(), name='password_reset_view'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html', success_url = 'accounts/login')),
]
