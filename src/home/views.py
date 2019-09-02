from django.shortcuts import render

from .models import Visitor
# Create your views here.


def index(request):
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_client_ip(request)
    print(ip)
    return render(request, 'home/index.html')
