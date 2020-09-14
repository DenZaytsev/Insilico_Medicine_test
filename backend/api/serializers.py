from rest_framework import serializers
from .models import OrderBrick, House


class HomeCreateSerializer(serializers.ModelSerializer):
    """Сериалайзер для создания домов"""
    class Meta:
        model = House
        fields = ('address', 'release_date')


class AddBricksSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = OrderBrick
        fields = ('brick_quantity', 'created_at')
