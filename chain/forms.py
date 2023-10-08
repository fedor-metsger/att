
from django import forms
from django.contrib import admin
from django.forms import ModelChoiceField

from dal import autocomplete

from chain.models import City, Country, Factory


def get_countries_list():
    countries = Country.objects.all().values("id", "name")
    return [[c["id"], c["name"]] for c in countries]


def get_cities_list():
    cities = City.objects.all().values('id','name','country__name')
    ret = [[c["id"], f'{c["name"]}, {c["country__name"]}'] for c in cities]
    return [[c["id"], f'{c["name"]}, {c["country__name"]}'] for c in cities]


class FactoryAdminForm(forms.ModelForm):
    city = autocomplete.Select2ListChoiceField(label="Город", choice_list=get_cities_list)

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["city"] = City.objects.get(pk=self.data["city"])
        return cleaned_data


class RetailerAdminForm(forms.ModelForm):
    city = autocomplete.Select2ListChoiceField(label="Город", choice_list=get_cities_list)

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["city"] = City.objects.get(pk=self.data["city"])
        return cleaned_data


class EntrepreneurAdminForm(forms.ModelForm):
    city = autocomplete.Select2ListChoiceField(label="Город", choice_list=get_cities_list)

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["city"] = City.objects.get(pk=self.data["city"])
        return cleaned_data
