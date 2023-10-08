
from django.contrib import admin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .forms import FactoryAdminForm, RetailerAdminForm, EntrepreneurAdminForm
from .models import Factory, Country, City, Product, Retailer, Entrepreneur


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["country"]
    search_fields = ["name"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "model", "published"]
    list_filter = ["factory"]
    search_fields = ["name", "model"]

@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    form = FactoryAdminForm
    model = Factory
    fields = ["name", "email", "city", "street", "building"]
    list_display = ["name", "country", "city", "creation_date"]
    list_filter = ["city"]
    search_fields = ["name"]

    def save_model(self, request, obj, form, change):
        obj.country_id = City.objects.get(pk=obj.city_id).country_id
        return super().save_model(request, obj, form, change)

@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    form = RetailerAdminForm
    model = Retailer
    fields = ["name", "email", "city", "street", "building", "factory", "debt"]
    list_display = ["name", "city", "factory", "debt"]
    list_filter = ["city"]
    search_fields = ["name"]
    actions = [clear_debt]

    def save_model(self, request, obj, form, change):
        obj.country_id = City.objects.get(pk=obj.city_id).country_id
        return super().save_model(request, obj, form, change)


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    form = EntrepreneurAdminForm
    model = Entrepreneur
    fields = ["name", "email", "city", "street", "building", "retailer", "debt"]
    list_display = ["name", "city", "retailer", "debt"]
    list_filter = ["city"]
    search_fields = ["name"]
    actions = [clear_debt]

    def save_model(self, request, obj, form, change):
        obj.country_id = City.objects.get(pk=obj.city_id).country_id
        return super().save_model(request, obj, form, change)
