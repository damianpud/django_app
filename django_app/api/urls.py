from django.urls import include, path
from rest_framework import routers
from api.views import ValidationView

router = routers.DefaultRouter()

urlpatterns = [
    path('validate/', ValidationView.as_view(), name='validate'),
    path('', include(router.urls))
]