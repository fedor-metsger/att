
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")

    def __str__(self):
        # return f'Country({self.name})'
        return f'{self.name}'

    class Meta:
        verbose_name = "страна"
        verbose_name_plural = "страны"



class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        # return f'City({self.name})'
        return f'{self.name}'

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    model = models.CharField(max_length=50, verbose_name='модель', null=True, blank=True)
    published = models.DateField(verbose_name='дата создания', auto_now_add=True)
    factory = models.ForeignKey("Factory", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        # return f'Product({self.name})'
        return f'{self.name}'

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"


class Factory(models.Model):
    name = models.CharField(max_length=100, verbose_name="наименование")
    email = models.EmailField(max_length=100, verbose_name="e-mail", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=100, verbose_name="улица", null=True, blank=True)
    building = models.CharField(max_length=10, verbose_name="дом", null=True, blank=True)
    creation_date = models.DateField(verbose_name="дата создания", auto_now_add=True)

    def __str__(self):
        # return f'Factory({self.name})'
        return f'{self.name}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class Retailer(models.Model):
    name = models.CharField(max_length=100, verbose_name="наименование")
    email = models.EmailField(max_length=100, verbose_name="e-mail", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=100, verbose_name="улица", null=True, blank=True)
    building = models.CharField(max_length=10, verbose_name="дом", null=True, blank=True)
    creation_date = models.DateField(verbose_name="дата создания", auto_now_add=True)
    factory = models.ForeignKey(Factory, verbose_name="завод", on_delete=models.SET_NULL, null=True)
    debt = models.DecimalField(verbose_name="задолженность", max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        # return f'Retailer({self.name})'
        return f'{self.name}'

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'


class Entrepreneur(models.Model):
    name = models.CharField(max_length=100, verbose_name="наименование")
    email = models.EmailField(max_length=100, verbose_name="e-mail", null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name="страна", on_delete=models.CASCADE)
    city = models.ForeignKey(City, verbose_name="город", on_delete=models.CASCADE)
    street = models.CharField(max_length=100, verbose_name="улица", null=True, blank=True)
    building = models.CharField(max_length=10, verbose_name="дом", null=True, blank=True)
    creation_date = models.DateField(verbose_name="дата создания", auto_now_add=True)
    retailer = models.ForeignKey(Retailer, verbose_name="розничная сеть", on_delete=models.SET_NULL, null=True)
    debt = models.DecimalField(verbose_name="задолженность", max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        # return f'Entrepreneur({self.name})'
        return f'{self.name}'

    class Meta:
        verbose_name = "предприниматель"
        verbose_name_plural = "предприниматели"
