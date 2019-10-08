from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from datetime import datetime

from .models import Wallpaper
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'bing/index.html'
    context_object_name = 'wallpapers'
    paginate_by = 9

    def get_queryset(self):
        has = Wallpaper.objects.filter(
            datetime__contains=timezone.now().date())
        if has.count() == 0:
            print('sipder is running')
            from .spider import spider
            spider()
        return Wallpaper.objects.all()


def detail(request, hsh):
    wallpaper = get_object_or_404(Wallpaper, hsh=hsh)
    return render(request, 'bing/detail.html', {'wallpaper': wallpaper})
