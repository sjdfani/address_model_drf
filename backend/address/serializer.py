from rest_framework import serializers
from .models import Address
from django.contrib.auth import get_user_model


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = '__all__'
