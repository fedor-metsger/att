
from rest_framework import serializers


class CityValidator():
    def __call__(self, value):
        country = value["country"]
        city = value["city"]
        if city.country_id != country.id:
            raise serializers.ValidationError(f'Город {city.name} не находится в стране {country.name}')


class DebtValidator():
    def __call__(self, value):
        if "debt" in value:
            raise serializers.ValidationError(f'Нельзя обновлять поле «Задолженность перед поставщиком» через API')
