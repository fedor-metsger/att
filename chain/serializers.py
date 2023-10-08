
from rest_framework import serializers

from chain.models import Factory, Retailer, Entrepreneur
from chain.validators import CityValidator, DebtValidator


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'
        validators = [CityValidator()]


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        exclude = ["debt"]
        validators = [CityValidator()]



class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        exclude = ["debt"]
        validators = [CityValidator()]
