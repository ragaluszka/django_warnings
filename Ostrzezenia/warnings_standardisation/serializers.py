from rest_framework import serializers
from .models import Warning, Voltage, Direction


class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warning
        fields = ['id', 'name']


class VoltageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voltage
        fields = ['id', 'name']


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ['id', 'name']


class WarningFullSerializer(serializers.ModelSerializer):
    voltage = VoltageSerializer(many=True, read_only=True)

    class Meta:
        model = Warning
        fields = ['id', 'name', 'voltage']
