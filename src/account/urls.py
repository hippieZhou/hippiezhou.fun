from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
