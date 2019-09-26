from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from pywxclient.core import Session, SyncClient
from common.decorators import ajax_required
# Create your views here.

client = None


def index(request):
    s1 = Session()
    global client
    client = SyncClient(s1)
    url = client.get_authorize_url()
    return render(request, 'wechat/index.html', {'url': url})


@ajax_required
@require_POST
def login(request):
    doamin = request.POST.get('domain')
    print(client.authorize())
    if doamin == 'hippiezhou.fun' and not client:
        return JsonResponse({'status': '1'})
    return JsonResponse({'status': '0'})


def logout(request):
    return
