from django.urls import include, path
from rest_framework import routers
from .views import AddressViewSet

app_name = 'address'

router = routers.SimpleRouter()
router.register('', AddressViewSet, basename='address')

urlpatterns = [
    path('', include(router.urls))
]
