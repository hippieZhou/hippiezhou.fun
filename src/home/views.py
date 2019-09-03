from django.shortcuts import render

from .models import Visitor
# Create your views here.


def index(request):
    ip = request.META.get('REMOTE_ADDR')
    a = Visitor.objects.all()
    visitor = Visitor.objects.get(ip=ip)
    if visitor is None:
        visitor = Visitor()
        visitor.ip = ip
    visitor.save()
    return render(request, 'home/index.html', {'ip': ip})
