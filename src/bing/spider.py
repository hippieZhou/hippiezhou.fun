import urllib
import requests
import json
import pytz

from django.db import transaction
from django.utils import timezone

from datetime import datetime

from .models import Wallpaper

WALLPAPER_BASE_URL = 'https://cn.bing.com'

USER_AGENG = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
COOKIES = "SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=550985DA3A594E778D50B0672C8B7B3C&dmnchg=1; _EDGE_V=1; MUID=1229F3F5A56B69751C77FE63A41468D4; MUIDB=1229F3F5A56B69751C77FE63A41468D4; ENSEARCH=BENVER=1; SerpPWA=reg=1; MSCC=1; MSTC=ST=1; _tarLang=default=zh-Hans; _EDGE_S=mkt=zh-cn&SID=2FDB4EA865B263983FA74332649C62ED; _FP=hta=on; ULC=P=1175F|7:3&H=1175F|7:3&T=1175F|7:3; ipv6=hit=1563175374895&t=4; SRCHHPGUSR=CW=1920&CH=947&DPR=1&UTC=480&WTS=63698768573; SRCHUSR=DOB=20190711&T=1563171781000; _SS=SID=2FDB4EA865B263983FA74332649C62ED&HV=1563171782&bIm=208"


def spider():
    print('开始请求。。。')
    headers = {
        "Host": "cn.bing.com",
        "User-Agent": USER_AGENG,
        'Cookie': COOKIES
    }

    params = urllib.parse.urlencode({
        'format': 'js',
        'idx': -1,
        'n': 8,
        'pid': 'hp',
        'mkt': 'en-US'
    })

    req = requests.get(
        'https://cn.bing.com/HPImageArchive.aspx', headers=headers, params=params)
    if req.status_code == 200:
        data = json.loads(req.text)
        bings = data.get('images', None)
        for item in bings:
            try:
                hsh = item.get('hsh', None)

                old = Wallpaper.objects.filter(hsh=hsh).first()
                if old is not None:
                    continue

                title = item.get('title', None)
                caption = item.get('caption', None)
                desc = item.get('desc', None)

                copyright = item.get('copyright', None)
                copyrightonly = item.get('copyrightonly', None)
                copyrightlink = item.get('copyrightlink', None)

                dt = datetime.strptime(
                    item.get('fullstartdate', timezone.now()), '%Y%m%d%H%M%S')

                quiz = item.get('quiz', None)
                url = item.get('url', None)
                urlbase = item.get('urlbase', None)

                wallpaper = Wallpaper()
                wallpaper.hsh = hsh
                wallpaper.title = title
                wallpaper.caption = caption
                wallpaper.desc = desc
                wallpaper.copyright = copyright
                wallpaper.copyrightonly = copyrightonly
                wallpaper.copyrightlink = copyrightlink
                wallpaper.datetime = timezone.make_aware(
                    dt, pytz.timezone('UTC'))
                wallpaper.quiz = quiz
                wallpaper.url = url
                wallpaper.urlbase = urlbase
                wallpaper.save()
            except Exception as e:
                print('spider:{0}'.format(e))
                transaction.rollback()
                continue
