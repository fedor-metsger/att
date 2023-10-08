# Generated by Django 4.2.5 on 2023-10-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chain", "0005_alter_entrepreneur_city_alter_entrepreneur_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="entrepreneur",
            name="debt",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="retailer",
            name="debt",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]