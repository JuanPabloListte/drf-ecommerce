# Generated by Django 5.0.1 on 2024-02-19 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_historicalproduct_category_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryproduct',
            name='measure_unit',
        ),
        migrations.RemoveField(
            model_name='historicalcategoryproduct',
            name='measure_unit',
        ),
    ]