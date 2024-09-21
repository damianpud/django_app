from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .throttling import CustomRateThrottle


class ValidationView(APIView):
    throttle_classes = [CustomRateThrottle]

    def post(self, request, *args, **kwargs):
        if not isinstance(self.request.data, list):
            return Response({
                "error": "Invalid data format, expected a list of dictionaries."
            }, status=status.HTTP_400_BAD_REQUEST)

        valid_count = sum(
            isinstance(item.get('num'), (int, float))
            and isinstance(item.get('text'), str)
            and item.get('num') is not None
            and item.get('text') is not None
            and item.get('text') != ''
            and set(item.keys()) == {'num', 'text'} for item in self.request.data
        )

        return Response({
            'valid': valid_count,
            'invalid': len(self.request.data) - valid_count,
        }, status=status.HTTP_200_OK)
