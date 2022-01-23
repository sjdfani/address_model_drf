from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Address
from .serializer import AddressSerializer, UserSerializer
from .permissions import IsSuperUser
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_permissions(self):
        if self.action not in ['list', 'retrieve']:
            permission_classes = [IsSuperUser, IsAdminUser]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]


class UserAddress(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
