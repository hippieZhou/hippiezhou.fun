from django.shortcuts import render
from django.utils import timezone

from datetime import datetime

from .spider import spider
from .models import Wallpaper
# Create your views here.


def index(request):
    first = Wallpaper.objects.first()
    print(first.datetime)
    if first is None:
        spider()
    else:
        if first.datetime.today().date() < datetime.today().date():
            spider()

    return render(request, 'bing/index.html', {
        'wallpapers': Wallpaper.objects.all()
    })
