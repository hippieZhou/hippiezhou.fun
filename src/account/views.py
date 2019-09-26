from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, 'account/register.html')


def dashboard(request):
    return render(request, 'account/dashboard.html')
