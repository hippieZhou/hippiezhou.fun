from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'bing'


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
]
