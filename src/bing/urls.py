from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'bing'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<hsh>/detail/', views.detail, name='detail'),
]
