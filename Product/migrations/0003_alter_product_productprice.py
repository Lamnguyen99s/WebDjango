# Generated by Django 4.0.6 on 2022-11-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_product_productname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productPrice',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]