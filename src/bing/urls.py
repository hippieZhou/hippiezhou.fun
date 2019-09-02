from django.urls import path
from django.views.generic import TemplateView

app_name = 'bing'


urlpatterns = [
    path('', TemplateView.as_view(template_name='bing/index.html'), name='index'),
]
