from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'wechat'
urlpatterns = [
    path('', views.index, name='index'),
    path('random/', views.random, name='random'),
]
