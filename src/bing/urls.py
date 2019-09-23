from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from . import views

app_name = 'bing'
urlpatterns = [
    path('', cache_page(60 * 15)(views.IndexView.as_view()), name='index'),
    path('detail/<hsh>/', cache_page(60 * 15)(views.detail), name='detail'),
]
