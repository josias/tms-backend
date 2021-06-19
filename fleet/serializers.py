from rest_framework import serializers
from .models import Car, Insurance, Tax, TechnicalCheckIn, Service


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        # for security select fields individually
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        # for security select fields individually
        fields = '__all__'


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        # for security select fields individually
        fields = '__all__'


class TechnicalCheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalCheckIn
        # for security select fields individually
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        # for security select fields individually
        fields = '__all__'

