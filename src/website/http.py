from django.utils.deprecation import MiddlewareMixin


class RemoteAddrFromForwardedForMiddleware(MiddlewareMixin):
    def process_request(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        request.META['REMOTE_ADDR'] = ip
