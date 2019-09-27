from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('goodbye/', TemplateView.as_view(template_name='account/goodbye.html'), name='goodbye')
]
