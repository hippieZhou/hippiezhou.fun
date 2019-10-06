from django.shortcuts import render

from .models import Visitor
# Create your views here.


def index(request):
    ip = request.META.get('REMOTE_ADDR')
    count = Visitor.objects.filter(ip=ip).count()
    if count == 0:
        visitor = Visitor()
        visitor.ip = ip
        visitor.save()
    return render(request, 'home/index.html', {'ip': ip})
