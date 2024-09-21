from rest_framework.throttling import AnonRateThrottle


class CustomRateThrottle(AnonRateThrottle):
    def allow_request(self, request, view):
        if request.headers.get('apikey') == 'rekrutacja2024':
            return True
        return super().allow_request(request, view)
