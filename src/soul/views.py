from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from common.decorators import ajax_required

from home.models import Soul
# Create your views here.


def index(request):
    return render(request, 'soul/index.html', {'soul': Soul.objects.random()})


@ajax_required
@require_GET
def random(request):
    return JsonResponse({'soul': Soul.objects.random().title})
