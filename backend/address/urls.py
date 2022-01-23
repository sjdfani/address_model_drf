from django.urls import include, path
from rest_framework import routers
from .views import AddressViewSet, UserAddress

app_name = 'address'

router = routers.SimpleRouter()
router.register('', AddressViewSet, basename='address')

urlpatterns = [
    path('', include(router.urls)),
    path('user', UserAddress.as_view()),
]
