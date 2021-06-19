from rest_framework import serializers
from .models import Organization, Employee, Mission, Fuel, Incident


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        # for security select fields individually
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # for security select fields individually
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        # for security select fields individually
        fields = '__all__'


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        # for security select fields individually
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        # for security select fields individually
        fields = '__all__'
