from django import template

register = template.Library()


@register.filter(name='bingimage')
def bingimage_filter(url: str):
    return url if url.startswith('http') else 'https://cn.bing.com{0}'.format(url)
