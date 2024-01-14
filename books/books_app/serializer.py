from rest_framework import serializers

from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = "__all__"

