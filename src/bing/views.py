from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime, timezone

from .models import Wallpaper
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'bing/index.html'
    context_object_name = 'wallpapers'
    paginate_by = 1

    def get_queryset(self):
        first = Wallpaper.objects.first()
        db_time = first.datetime.timestamp()
        local_time = datetime.now(timezone.utc).timestamp()
        if first is None or db_time <= local_time:
            print(db_time, local_time)
            from .spider import spider
            spider()
        return Wallpaper.objects.all()
