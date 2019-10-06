from django.shortcuts import render
from django.conf import settings

from .models import Visitor
# Create your views here.


def index(request):
    ip = request.META.get('REMOTE_ADDR')
    try:
        visitor = Visitor.objects.get(ip=ip)
    except Visitor.DoesNotExist:
        visitor = Visitor()
        visitor.ip = ip
    if not settings.DEBUG:
        visitor.save()
    return render(request, 'home/index.html', {'ip': ip})
