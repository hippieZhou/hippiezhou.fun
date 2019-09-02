from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'home'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='home/about.html'), name='about'),
]
