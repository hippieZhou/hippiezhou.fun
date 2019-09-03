from django.shortcuts import render
from django.utils import timezone

from datetime import datetime

from .spider import spider
from .models import Wallpaper
# Create your views here.


def index(request):
    first = Wallpaper.objects.first()
    if first is None or first.datetime.date() < datetime.today().date():
        spider()

    return render(request, 'bing/index.html', {
        'wallpapers': Wallpaper.objects.all()
    })
