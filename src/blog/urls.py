from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:id>/<str:slug>/', views.detail, name='detail'),
]
