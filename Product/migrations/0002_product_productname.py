# Generated by Django 4.0.6 on 2022-11-11 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productName',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
