"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('bing/', include('bing.urls', namespace='bing')),
    path('wechat/', include('wechat.urls', namespace='wechat')),
    path('blog/', include('blog.urls', namespace='blog')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('jet/', include('jet.urls', namespace='jet')),

    path('admin/', admin.site.urls),
]

handler404 = 'website.error_views.handler404'
handler500 = 'website.error_views.handler500'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "Attention Admin"
admin.site.site_header = "Attention Admin"
